import psutil
import GPUtil
import tkinter

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

    return GetCPU() + "\n" + GetRAM() + "\n" + GetGPU()

main = tkinter.Tk()
main.title("StatusMonitor")
height = main.winfo_screenheight()
width = main.winfo_screenwidth()
size = str(int(width / 5)) + "x" + str(int(height / 4))
main.geometry(size)

menubar = tkinter.Menu(main)
filemenu = tkinter.Menu(menubar, tearoff=0)

var = tkinter.StringVar()


def show():
    global var
    text = status()
    main.after(100, show)
    var.set(text)


show()
l = tkinter.Label(main, textvariable=var, font=('Arial', int(width / 75)))
l.pack()

main.mainloop()
