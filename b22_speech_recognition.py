import speech_recognition as sr


def main():
    sound = 'E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/b22_bangla1.flac'
    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        print('converting audio to text .... ')

        audio = r.listen(source)
        content = [None] * 5
        content[0] = r.recognize_google(audio, language='bn-BD')
        content[1] = r.recognize_houndify(audio, 'VMlpQlaja5rjLeJFR2mm-Q==', 'nU-uxwQze0BtT6ZG4v_e7dV7zp92C6qS3w66Ycqg6bChrN0FeCc1SoRm-ht-AUDiAko3nm8f30GNG1Cq8p2vMg==')  # Houndify by SoundHound
        # content[2] = r.recognize_ibm(audio, language='bn-BD')  # IBM Speech to Text
        # content[3] = r.recognize_sphinx(audio, language='bn-BD')  # CMU Sphinx - requires installing PocketSphinx
        # content[4] = r.recognize_wit(audio, language='bn-BD')  # Wit.ai

    for i in content:
        print('converted audio is: {}'.format(i))


if __name__ == "__main__":
    main()