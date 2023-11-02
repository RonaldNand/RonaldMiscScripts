#! /bin/bash

##### Install Dependency

sudo apt update && sudo apt install ffmpeg

#### Create Conda Evironment

$envname = 'whisper'

conda create -n $envname python=3.9

conda activate $envname

#### Install Whisper to Conda Environment

pip install -U openai-whisper

#### Download Models

whisper dummy.mp3 --model tiny
whisper dummy.mp3 --model tiny.en
whisper dummy.mp3 --model base
whisper dummy.mp3 --model base.en
whisper dummy.mp3 --model small
whisper dummy.mp3 --model small.en
whisper dummy.mp3 --model medium
whisper dummy.mp3 --model medium.en
whisper dummy.mp3 --model large

