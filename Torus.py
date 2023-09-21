import math
import sys

# Constants
pi = math.pi
theta_spacing = 0.07
phi_spacing = 0.02
screen_width = 80
screen_height = 24
R1 = 1
R2 = 2
K2 = 5
K1 = screen_width * K2 * 3 / (8 * (R1 + R2))

def render_frame(A, B):
    # Precompute sines and cosines of A and B
    cosA = math.cos(A)
    sinA = math.sin(A)
    cosB = math.cos(B)
    sinB = math.sin(B)

    # Initialize the output and z-buffer
    output = [[' ' for _ in range(screen_height)] for _ in range(screen_width)]
    zbuffer = [[0 for _ in range(screen_height)] for _ in range(screen_width)]

    for theta in range(int(2 * pi / theta_spacing)):
        costheta = math.cos(theta * theta_spacing)
        sintheta = math.sin(theta * theta_spacing)

        for phi in range(int(2 * pi / phi_spacing)):
            cosphi = math.cos(phi * phi_spacing)
            sinphi = math.sin(phi * phi_spacing)

            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            # Final 3D (x, y, z) coordinates after rotations
            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z  # "One over z"

            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 - K1 * ooz * y)

            # Calculate luminance based on the formulas in https://www.a1k0n.net/2011/07/20/donut-math.html
            L = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB * (cosA * sintheta - costheta * sinA * sinphi)

            if L > 0 and ooz > zbuffer[xp][yp]:
                zbuffer[xp][yp] = ooz
                luminance_index = int(L * 8)
                output[xp][yp] = ".,-~:;=!*#$@"[luminance_index]

    # Print the frame to the console
    sys.stdout.write('\x1b[H')
    for j in range(screen_height):
        for i in range(screen_width):
            sys.stdout.write(output[i][j])
        sys.stdout.write('\n')

if __name__ == "__main__":
    A, B = 0, 0
    while True:
        render_frame(A, B)
        A += 0.04
        B += 0.02
