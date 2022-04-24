import pyautogui as pgi
import time

def mouse_down(a):
    pgi.moveTo(int(a[0]), int(a[1]))
    pgi.mouseDown(button=a[2])

def mouse_up(a):
    pgi.moveTo(int(a[0]), int(a[1]))
    pgi.mouseUp(button=a[2])

def key_down(a):
    if ":" in a:
        a = a.split(':')
        pgi.hotkey(a[0],a[1])
    else:
        pgi.keyDown(a)

def key_up(a):
    pgi.keyUp(a)

# def f(a):
#     pgi.

def handler(func, *argv):
    return func(*argv)


def activator(_filename):
    f = open(f"./log/{_filename}.log", 'r')

    log = []

    for line in f:
        line = line.rstrip()
        l = line.split(",")
        log.append(l)

    f.close()

    log = activate(log)

    # print(log)
    
    elapsed_time = 0

    for i in log:
        print(float(i[0])-elapsed_time)
        if float(i[0])-elapsed_time >=0:
            time.sleep(float(i[0])-elapsed_time)

        start_time = time.perf_counter()
        handler(i[3], i[2])
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        
    # pgi.alert(text='sample', title='sample', button='OK')
    return True


def activate(_log):
    for i in range(len(_log)):
        if "Key." in _log[i][2]:
            _log[i][2] = _log[i][2][4:]
            # continue

        if "_" in _log[i][2]:
            _log[i][2] = _log[i][2].strip("_")
            # continue

        if "shift" == _log[i][2]:
            _log[i][2] = "shiftleft"
            continue

        if "shiftr" == _log[i][2]:
            _log[i][2] = "shiftright"
            continue

        if "ctrlr" == _log[i][2]:
            _log[i][2] = "ctrlright"
            continue

        if "ctrll" == _log[i][2]:
            _log[i][2] = "ctrlleft"
            continue

        if "altgr" == _log[i][2]:
            _log[i][2] ="optionright"
            continue

        if "altl" == _log[i][2]:
            _log[i][2] ="optionleft"
            continue

        if "cmd" == _log[i][2]:
            _log[i][2] = "command"
            continue

        if "<28>" == _log[i][2]:
            _log[i][2] = "nonconvert"
            continue

        if "<29>" == _log[i][2]:
            _log[i][2] = "convert"

        if "\x01" ==  _log[i][2]:
            _log[i][2] = "ctrl:a"
        if "\x02" ==  _log[i][2]:
            _log[i][2] = "ctrl:b"
        if "\x03" ==  _log[i][2]:
            _log[i][2] = "ctrl:c"
        if "\x04" ==  _log[i][2]:
            _log[i][2] = "ctrl:d"
        if "\x05" ==  _log[i][2]:
            _log[i][2] = "ctrl:e"
        if "\x06" ==  _log[i][2]:
            _log[i][2] = "ctrl:f"
        if "\x07" ==  _log[i][2]:
            _log[i][2] = "ctrl:g"
        if "\x08" ==  _log[i][2]:
            _log[i][2] = "ctrl:h"
        if "\x09" ==  _log[i][2]:
            _log[i][2] = "ctrl:i"
        if "\x0A" ==  _log[i][2]:
            _log[i][2] = "ctrl:j"
        if "\x0B" ==  _log[i][2]:
            _log[i][2] = "ctrl:k"
        if "\x0C" ==  _log[i][2]:
            _log[i][2] = "ctrl:l"
        if "\x0D" ==  _log[i][2]:
            _log[i][2] = "ctrl:m"
        if "\x0E" ==  _log[i][2]:
            _log[i][2] = "ctrl:n"
        if "\x0F" ==  _log[i][2]:
            _log[i][2] = "ctrl:o"
        if "\x10" ==  _log[i][2]:
            _log[i][2] = "ctrl:p"
        if "\x11" ==  _log[i][2]:
            _log[i][2] = "ctrl:q"
        if "\x12" ==  _log[i][2]:
            _log[i][2] = "ctrl:r"
        if "\x13" ==  _log[i][2]:
            _log[i][2] = "ctrl:s"
        if "\x14" ==  _log[i][2]:
            _log[i][2] = "ctrl:t"
        if "\x15" ==  _log[i][2]:
            _log[i][2] = "ctrl:u"
        if "\x16" ==  _log[i][2]:
            _log[i][2] = "ctrl:v"
        if "\x17" ==  _log[i][2]:
            _log[i][2] = "ctrl:w"
        if "\x18" ==  _log[i][2]:
            _log[i][2] = "ctrl:x"
        if "\x19" ==  _log[i][2]:
            _log[i][2] = "ctrl:y"
        if "\x1A" ==  _log[i][2]:
            _log[i][2] = "ctrl:z"

    for i in range(len(_log)):
        if 'Button.left.True' == _log[i][1]:
            _log[i][2] = _log[i][2].split(':')+['left']
            _log[i].append(mouse_down)
            continue

        if 'Button.left.False' == _log[i][1]:
            _log[i][2] = _log[i][2].split(':')+['left']
            _log[i].append(mouse_up)
            continue
            
        if 'Button.right.True' == _log[i][1]:
            _log[i][2] = _log[i][2].split(':')+['right']
            _log[i].append(mouse_down)
            continue

        if 'Button.right.True' == _log[i][1]:
            _log[i][2] = _log[i][2].split(':')+['right']
            _log[i].append(mouse_up)
            continue
        
        if 'Key.True' == _log[i][1]:
            _log[i].append(key_down)
            continue
        
        if 'Key.False' == _log[i][1]:
            _log[i].append(key_up)

    return _log
    

if __name__ == "__main__":
    activator("Sun,24,Apr,2022,03,18,01")