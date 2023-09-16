import math
import time

def main():
    A = 0
    B = 0
    z = [0.0] * 1760
    b = [' '] * 1760
    print("\x1b[2J", end='', flush=True)
    
    while True:
        b = [' '] * 1760
        z = [0.0] * 7040
        # nested loops
        for j in range(int(6.28 / 0.07)):
            for i in range(int(6.28 / 0.02)):
                # some trig bullshit
                c = math.sin(i)
                d = math.cos(j)
                e = math.sin(A)
                f = math.sin(j)
                g = math.cos(A)
                h = d + 2
                D = 1 / (c * h * e + f * g + 5)
                l = math.cos(i)
                m = math.cos(B)
                n = math.sin(B)
                t = c * h * g - f * e
                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))
                o = x + 80 * y
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                
                if 22 > y > 0 and x > 0 and 80 > x and D > z[o]:
                    z[o] = D
                    b[o] = ".,-~:;=!*#$@"[N] if N > 0 else " "
        
        print("\x1b[H", end='', flush=True)
        for k in range(1761):
            print(b[k], end='' if k % 80 else '\n', flush=True)
            A += 0.00004
            B += 0.00002
        
        time.sleep(0.03)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
