import wave,pyaudio


class recordWave():
    # 设置
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.RATE = 16000
        self.CHANNELS = 1
        self.RECORD_SECONDS = 3

    # 录音函数
    def record(self):
        pa = pyaudio.PyAudio()
        stream = pa.open(format=self.FORMAT,
                         channels=self.CHANNELS,
                         rate=self.RATE,
                         input=True,
                         frames_per_buffer=self.CHUNK)
        print('聆听命令...')
        buffer = []
        for i in range(0, int(self.RATE/self.CHUNK*self.RECORD_SECONDS)):
            audio_data = stream.read(self.CHUNK)
            buffer.append(audio_data)
        print('听到命令，正在识别')
        stream.stop_stream()
        stream.close()
        pa.terminate()
        wf = wave.open('record.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(pa.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(buffer))
        wf.close()
if __name__ == '__main__':
    recordWave().record()