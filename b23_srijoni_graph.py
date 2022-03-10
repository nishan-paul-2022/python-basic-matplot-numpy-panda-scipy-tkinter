import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile
import matplotlib
import datetime
plt.style.use('seaborn-whitegrid')
plt.rcParams.update({'font.size': 20})


def timeTicks(x, pos):
    d = datetime.timedelta(seconds=x)
    return str(d)


def graph_training_validation():  # Many plot types can be combined in one figure to create powerful and flexible representations of data.
    x1 = [i for i in range(20)]
    y1 = [0, 7.07, 12.31, 16.11, 20.89, 24.99, 28.54, 32.05, 36.78, 40.47, 44.77, 48.16, 52.63, 56.85, 60.00, 64.10, 68.33, 72.25, 75.10, 83.23]

    x2 = [i for i in range(20)]
    y2 = [37.66, 41.45, 42.89, 43.01, 45.23, 46.97, 48.31, 49.04, 51.39, 53.53, 55.78, 57.99, 59.07, 61.47, 63.89, 65.91, 67.01, 69.56, 70.17, 71.35]

    fig, ax = plt.subplots()
    fig.suptitle('ACCURACY')

    ax.plot(x1, y1, label='TRAINING ACCURACY')
    ax.plot(x2, y2, label='VALIDATION ACCURACY')
    ax.set_xlabel('EPOCH')
    ax.set_ylabel('EPOCH ACCURACY')
    plt.legend()

    plt.show()


def graph_wer():  # Many plot types can be combined in one figure to create powerful and flexible representations of data.
    x1 = [i for i in range(20)]
    y1 = [80.15, 72.11, 66.29, 63.01, 59.56, 54.55, 51.06, 47.00, 42.99, 40.05, 37.77, 35.23, 34.81, 33.03, 32.22, 31.49, 30.50, 29.79, 28.01, 27.46]

    x2 = [i for i in range(20)]
    y2 = [60.05, 57.11, 53.13, 47.78, 43.34, 40.04, 38.50, 37.06, 38.01, 37.79, 36.29, 35.31, 34.01, 33.99, 32.91, 32.77, 31.99, 31.07, 30.41, 30.07]

    fig, ax = plt.subplots()
    fig.suptitle('WORD ERROR RATE (WER)')

    ax.plot(x1, y1, label='TRAINING WORD ERROR RATE')
    ax.plot(x2, y2, label='VALIDATION WORD ERROR RATE')
    ax.set_xlabel('EPOCH')
    ax.set_ylabel('WORD ERROR RATE (WER)')
    plt.legend()

    plt.show()


def specgram_for_audio(fname):
    cmap = plt.get_cmap('viridis')  # this may fail on older versions of matplotlib
    vmin = -40  # hide anything below -40 dB
    cmap.set_under(color='k', alpha=None)

    rate, frames = wavfile.read(fname)
    fig, ax = plt.subplots()
    fig.suptitle(fname)
    ax.specgram(frames, Fs=rate, cmap=cmap, vmin=vmin)
    ax.axis('tight')

    ax.set_xlabel('TIME')
    ax.set_ylabel('FREQUENCY kHz')

    scale = 1e3  # KHz
    ticks = matplotlib.ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x / scale))
    ax.yaxis.set_major_formatter(ticks)

    formatter = matplotlib.ticker.FuncFormatter(timeTicks)
    ax.xaxis.set_major_formatter(formatter)
    plt.show()


if __name__ == '__main__':
    graph_training_validation()
    graph_wer()
    specgram_for_audio('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/b23_16khz_sample.wav')
    specgram_for_audio('E:/CODE/PYTHON/2021/data-done-tutorial-basic-matplot-numpy-panda-scipy-tkinter/b23_44khz_sample.wav')
