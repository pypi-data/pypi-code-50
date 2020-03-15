import torch


def get_gpu_nums():
    return torch.cuda.device_count()


def get_gpus_info():
    if torch.cuda.is_available():
        import os
        os.system("nvidia-smi")

        print("------------------------------------------------------")
        print("Available GPUs nums: ", torch.cuda.device_count(), "\n"
                                                                  "Current use GPUs: ", torch.cuda.current_device())

        print("GPUs devices names: ")
        for i in range(torch.cuda.device_count()):
            print("         ", torch.cuda.get_device_name(i))

        print('Memory Usage:')
        print('          Allocated:', round(torch.cuda.memory_allocated(0) / 1024 ** 3, 1), 'GB')
        print('          Cached:   ', round(torch.cuda.memory_cached(0) / 1024 ** 3, 1), 'GB')
        print("------------------------------------------------------")

    else:
        print("GPU is not available or no GPUs!")




if __name__ == "__main__":
    get_gpus_info()

    torch.load("../")
