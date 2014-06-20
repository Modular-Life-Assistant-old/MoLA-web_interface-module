class Module:
    def __init__(self):
        print('init')

    def load_configuration(self):
        print('load_configuration')

    def thread_1(self):
        while True:
            print('thread 1')
            time.sleep(1)
