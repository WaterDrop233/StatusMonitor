import psutil
import GPUtil

def status():
    def GetRAM():
        RAMFree = str(round(psutil.virtual_memory().free / 1024 ** 3, 1))
        RAMUsed = str(round(psutil.virtual_memory().used / 1024 ** 3, 1))
        RAMStatus = "内存:已用:" + RAMUsed + "GB" + "\n" + "     未用:" + RAMFree + "GB"
        return RAMStatus


    def GetCPU():
        CPUStatus = "CPU:已用:" + str(psutil.cpu_percent(interval=0.2))
        return CPUStatus


    def GetGPU():
        if len(GPUtil.getGPUs()) != 0:
            GPUStatus = "显卡:负载率:" + str(round(GPUtil.getGPUs()[0].load, 1)) + "\n" + "     显存使用率:" + str(round(GPUtil.getGPUs()[0].memoryUtil, 1))
        else:
            GPUStatus = "未检测到显卡"
        return GPUStatus

    return str(GetCPU() + "\n" + GetRAM() + "\n" + GetGPU())


