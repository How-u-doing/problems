// taken from https://github.com/vadimcn/vscode-lldb/wiki/Data-visualization
#include <complex>
#include <iostream>

/*
 * The Mandelbrot set is the set of values of c, under the iteration
 * z_{n+1} <- z_{n}^2 + c, with z_{0} = 0, which remains bounded for
 * all n > 0.
 * Easy to see that a point c belongs to the Mandelbrot set M iff
 * |z| <= 2, for all n >= 0. Thus, |c| = |z_{1}| <= 2. Furthermore,
 * it can be shown that the intersection of the set M with the real
 * axis (and thus also {Re(c) | c in M}) is precisely the interval
 * [-2, 1/4].
 */
void mandelbrot(int image[], int xdim, int ydim, int max_iter)
{
    for (int y = 0; y < ydim; ++y) {
        for (int x = 0; x < xdim; ++x) {
            // testing point c: Re(c) in [-2.2, 0.8], Im(c) in [-1.5, 1.5]
            std::complex<float> c(-2.2 + 3.0 * x / xdim, -1.5 + 3.0 * y / ydim);
            std::complex<float> z(0, 0);
            int iters = max_iter;
            for (int i = 0; i < max_iter; ++i) {
                z = z * z + c;
                if (std::abs(z) >= 2) {
                    iters = i;
                    break;
                }
            }
            image[y * xdim + x] = iters;
        }
    }
}

#define RED      "\033[31m"
#define GREEN    "\033[32m"
#define YELLOW   "\033[33m"
#define BLUE     "\033[34m"
#define MAGENTA  "\033[35m"
#define CYAN     "\033[36m"
#define END      "\033[0m"
#define COLORED_TEXT(text, color) color << text << END

int main()
{
    // play around with these parameters
    const int xdim = 500;
    const int ydim = 500;
    const int max_iter = 100;
    int image[xdim * ydim] = {};
    mandelbrot(image, xdim, ydim, max_iter);
    for (int y = 0; y < ydim; y += 10) {
        for (int x = 0; x < xdim; x += 5) {
            // draw a colorful plot according to the number of iterations
            const int iters = image[y * xdim + x];
            if (iters < max_iter * 0.125)
                std::cout << COLORED_TEXT('.', CYAN);
            else if (iters < max_iter * 0.25)
                std::cout << COLORED_TEXT('*', MAGENTA);
            else if (iters < max_iter * 0.5)
                std::cout << COLORED_TEXT('*', BLUE);
            else if (iters < max_iter * 0.75)
                std::cout << COLORED_TEXT('*', YELLOW);
            else if (iters < max_iter)
                std::cout << COLORED_TEXT('*', GREEN);
            else
                std::cout << COLORED_TEXT('*', RED);
        }
        std::cout << '\n';
    }
    return 0;
}
