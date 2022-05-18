"""
Created on Sat Mar 26 17:13:22 2022

@author: thereturn932
"""
from PyQt5.QtCore import QObject, pyqtSignal
import os
from PIL import Image
import moviepy.video.io.ImageSequenceClip
import random
import json
import numpy as np


class Generator(QObject):

    finished = pyqtSignal()
    progress = pyqtSignal(int)
    progressPerVideo = pyqtSignal(int)
    progressStatus = pyqtSignal(str)
    error = pyqtSignal(str)

    def generateFrame(self, subDirs, randomBackground, outputFolderNameFrames):

        layers = [[] for i in range(len(subDirs))]
        if randomBackground is True:
            color = tuple(np.random.choice(range(256), size=3))
        else:
            color = tuple(0, 0, 0)
        for i in range(len(subDirs)):
            # print(subDirs[i])
            for name in os.listdir(subDirs[i]):
                tempLayer = Image.open(os.path.join(subDirs[i], name))
                layers[i].append(tempLayer)

        if not os.path.exists(outputFolderNameFrames):
            os.mkdir(outputFolderNameFrames)

        for i in range(0, len(os.listdir(subDirs[i]))):
            final = Image.new("RGBA", layers[0][0].size, color)
            for layer in layers:
                final = Image.alpha_composite(final, layer[i])
            outDir = os.path.join(outputFolderNameFrames, f"{i:04d}.png")
            final.save(outDir)
            self.progressStatus.emit(f"{outDir}.png Created")

    def createVideo(self, frameDir, _id, outDir, _fps):
        image_files = [os.path.join(frameDir, img)
                       for img in os.listdir(os.path.join(frameDir))
                       if img.endswith(".png")]
        # print(image_files)
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(
            image_files, fps=_fps)
        if not os.path.exists(os.path.join(outDir, "videos")):
            os.mkdir(os.path.join(outDir, "videos"))
        clip.write_videofile(os.path.join(outDir, "videos", f"{_id}.mp4"))

    def createMetadata(self,
                       _name,
                       _description,
                       _id,
                       _attributes,
                       _uri="ipfs://CID/",
                       _videoOut=""):
        metadata = {
            "id": _id,
            "name": _name,
            "description": _description,
            "image": f"{_uri}{_id}.mp4",
            "attributes": _attributes
        }
        if not os.path.exists(os.path.join(_videoOut, "metadata")):
            os.mkdir(os.path.join(_videoOut, "metadata"))
        with open(os.path.join(_videoOut, "metadata", f"{_id}.json"),
                  "w") as write_file:
            json.dump(metadata, write_file, indent=4)

    def updateMetadata(self,
                       _name,
                       _description,
                       _metadataFolder,
                       _uri="ipfs://CID/"):
        for file in os.listdir(_metadataFolder):
            if file.endswith(".json"):
                # print(str(file))
                _id = str(file).split('.')[0]
                with open(os.path.join(_metadataFolder, file),
                          "r") as jsonFile:
                    data = json.load(jsonFile)
                if(_uri[-1] == "/"):
                    data["image"] = f"{_uri}{_id}.mp4"
                else:
                    data["image"] = f"{_uri}/{_id}.mp4"
                data["name"] = _name
                data["description"] = _description
                with open(os.path.join(_metadataFolder, file),
                          "w") as jsonFile:
                    json.dump(data, jsonFile, indent=4, separators=(',', ': '))
                self.progressStatus.emit(f"Updated {file}")

    def checkSize(self, layerDirs, generateNo):
        items = []
        for layerDir in layerDirs:
            items.append(len(next(os.walk(layerDir))[1]))
        maxGeneration = np.prod(items)
        if(maxGeneration < generateNo):
            return False
        else:
            return True

    def main(self,
             colName,
             colDesc,
             baseUri,
             frameOutDir,
             videoOutDir,
             fps,
             layers,
             layerDirs,
             randomBackground,
             generatedNo=1):
        DNA = []

        for k in range(0, generatedNo):
            randomNo = []
            subs = []
            for layerDir in layerDirs:
                items = next(os.walk(layerDir))[1]
                randomNo.append(random.randint(0, len(items) - 1))
            checkRes = self.checkSize(layerDirs, generatedNo)
            if not checkRes:
                self.error.emit(
                    "Requested generation count is higher "
                    "than maximum possible generations!"
                )
                self.finished.emit
                return
            # print(f"Craeting {k+1}. video!")
            self.progress.emit(round((k) / generatedNo * 100))
            # statusText.setText(f"Craeting {k+1}. video!")
            attributes = []
            _dna = ''.join(map(str, randomNo))
            while(_dna in DNA):
                # print(f"DNA {_dna} exists.")
                self.progressStatus.emit(f"Created {_dna}")
                randomNo = []
                for layerDir in layerDirs:
                    items = next(os.walk(layerDir))[1]
                    randomNo.append(random.randint(0, len(items) - 1))
                    _dna = ''.join(map(str, randomNo))
            for i in range(len(layerDirs)):
                items = next(os.walk(layerDirs[i]))[1]
                subs.append(os.path.join(layerDirs[i], items[randomNo[i]]))
                attributes.append({
                    "trait_type": layers[i],
                    "value": items[randomNo[i]]
                })
            self.generateFrame(subs, randomBackground,
                               f"{str(frameOutDir)}/{k + 1}")
            frame_dir = f"{str(frameOutDir)}/{k + 1}"
            self.createVideo(frame_dir, (k + 1), str(videoOutDir), fps)
            self.createMetadata(_name=colName, _description=colDesc,
                                _id=str(k + 1), _attributes=attributes,
                                _uri=baseUri, _videoOut=videoOutDir)
            # print(f"Created {_dna}")
            DNA.append(_dna)
            self.progress.emit(round((k + 1) / generatedNo * 100))
            self.progressStatus.emit(f"Created {_dna}")
        self.finished.emit
