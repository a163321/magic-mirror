import wave
from pyaudio import PyAudio, paInt16
import yuyin
import tuling


class Voice():

    def __init__(self):
        self.framerate = 16000
        self.NUM_SAMPLES = 1024
        self.channels = 1
        self.sampwidth = 2
        self.TIME = 3
        self.chunk = 2014

    def save_wave_file(self, filename, data):
        '''save the date to the wavfile'''
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.sampwidth)
        wf.setframerate(self.framerate)
        wf.writeframes(b"".join(data))
        wf.close()

    def my_record(self):
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1,
                         rate=self.framerate, input=True,
                         frames_per_buffer=self.NUM_SAMPLES)
        my_buf = []
        count = 0
        # print('听取命令中')
        while count < self.TIME * 20:  # 控制录音时间
            string_audio_data = stream.read(self.NUM_SAMPLES)
            my_buf.append(string_audio_data)
            count += 1
            # print('.')
        self.save_wave_file('01.wav', my_buf)
        stream.close()

    def play(self):
        wf = wave.open(r"auido.mp3", 'rb')
        p = PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
        while True:
            data = wf.readframes(self.chunk)
            if data == "":
                break
            stream.write(data)
        stream.close()
        p.terminate()


if __name__ == '__main__':
    while True:
        voice = Voice()
        voice.my_record()
        print('Over!')
        # play()
        s = yuyin.Baiduyuyin().asr('01.wav')['result'][0]
        a = tuling.Tuling().get_answer(s)
        # yuyin.Baiduyuyin().synthesis(a)

        print(a)
