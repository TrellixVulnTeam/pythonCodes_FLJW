import numpy as np 

cdef inline double norm2(double complex z):
    return z.real*z.real+z.imag*z.imag

cdef int escape(double complex z,
                double complex c,
                double zmax,
                int nmax):
    cdef:
        int i = 0
        double square_zmax = zmax*zmax
    while norm2(z) < zmax and i < nmax:
        z = z*z+c
        i += 1
    return i

def calc_julia(int resolution,
                double complex c,
                double bound=1.5,
                double zmax=4.0,
                int nmax=1000):
    cdef:
        double step = 2.0*bound/resolution
        int i, j
        double complex z
        double real, imag
        int[:, ::1] counts

    counts = np.zeros((resolution+1, resolution+1), dtype=np.int32)

    for i in range(resolution+1):
        real = -bound+i*step
        for j in range(resolution+1):
            imag = -bound+j*step
            z = real+imag*1j
            counts[i, j] = escape(z, c, zmax, nmax)

    return np.asarray(counts)
