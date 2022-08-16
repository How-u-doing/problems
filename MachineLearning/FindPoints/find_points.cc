/*
 * The image.png is made up of a regular points grid with 3 special points.
 * Now let's try to find those 3 special points.
 *
 * A machine learning approach shall be implemented in the future :^)
 */

#include <vector>
#include <algorithm>
#include <map>
#include <utility>
#include <iostream>
#include <cstddef>
#include <cassert>

struct Point {
    int x_;
    int y_;

    Point(int x, int y) : x_(x), y_(y) {}
};

int determine_ncols_of_original_grid(const std::vector<int>& raws)
{
    assert(raws.size() > 6 && "# of raws < 7, need to seek other approaches");
    // we can determine ncols using at most 7 raws (the 3 specail points
    // were on 3 different raws)
    std::map<int, int> m;
    for (int i = 0; i < 7; ++i) {
        ++m[raws[i]];
    }
    for (const auto& x : m) {
        if (x.second >= 4)
            return x.first;
    }
    return -1; // corrupted data
}

// It's reasonable to asssume that the original grid is an m-by-n matrix
// of points, where m,n >= 10 :)
void find_points_sorted(const std::vector<Point>& all_points,
                        std::vector<Point>& special_points)
{
    assert(special_points.size() == 0);

    // obtain the column number of each raw
    std::vector<int> raws(1, 1); // raws[i] := # of columns in raw i
    const size_t N = all_points.size();
    for (size_t i = 1, raw_no = 0; i < N; ++i) {
        if (all_points[i-1].y_ != all_points[i].y_) {
            ++raw_no;
            raws.push_back(1);
        }
        else {
            ++raws[raw_no];
        }
    }

    int grid_cols = determine_ncols_of_original_grid(raws);
    assert(grid_cols != -1 && "corrupted data");

    // find which raw(s) contain those 3 special points
    std::vector<std::pair<size_t, size_t>> special_raws;
    int grid_delta_x = 0, grid_x_min = 0, grid_x_max = 0;
    for (size_t i = 0, npoints = 0; i < raws.size(); ++i) {
        if (raws[i] != grid_cols) { // raws[i] == [grid_cols+][1-3]
            special_raws.emplace_back(i, npoints);
        }
        else if (grid_delta_x == 0) {
            grid_delta_x = all_points[npoints+1].x_ -
                           all_points[npoints].x_;
            grid_x_min = all_points[npoints].x_;
            grid_x_max = all_points[npoints + raws[i]-1].x_;
        }
        npoints += raws[i];
    }

    // obtain the special points from the special raws
    for (size_t i = 0, k = 0; i < raws.size(); ++i) {
        if (i == special_raws[k].first) {
            const int base = special_raws[k].second;
            const int raw_end = base + raws[i];
            if (raws[i] <= 3) {
                for (int j = base; j < raw_end; ++j) {
                    special_points.push_back(all_points[j]);
                }
            }
            else { // raws[i] == grid_cols + [1-3]
                for (int j = base; j < raw_end; ++j) {
                    if (all_points[j].x_ < grid_x_min || // left
                        (all_points[j].x_ - grid_x_min)  // inside or
                        % grid_delta_x != 0 ||           // right
                        all_points[j].x_ > grid_x_max)   // right
                        special_points.push_back(all_points[j]);
                }
            }
            if (special_points.size() == 3) // find all
                return;
            if (k < special_raws.size()-1)
                ++k;
        }
    }
}

// NB: Our solution can only handle well-placed grids (that is, coordinates
// x (y) of each column (row) are all the same). Otherwise, more sophisticated
// approaches must be developed (e.g. rotate the grid first, find the
// (transformed) special points, then transform the points back).
void find_points(const std::vector<Point>& all_points,
                 std::vector<Point>& special_points)
{
#if !POINTS_SORTED
    std::vector<Point> sorted_all_points(all_points);
    std::sort(sorted_all_points.begin(), sorted_all_points.end(),
              [] (const Point& lhs, const Point& rhs) {
                  return lhs.y_ < rhs.y_ ||
                         (lhs.y_ == rhs.y_ && lhs.x_ < rhs.x_);
              });
    find_points_sorted(sorted_all_points, special_points);
#else
    find_points_sorted(all_points, special_points);
#endif
}

std::vector<Point> create_grid(int m, int n, int x0, int y0,
                               int delta_x = 2, int delta_y = 2)
{
    std::vector<Point> grid;
    grid.reserve(m * n);
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            grid.emplace_back(x0 + j * delta_x, y0 + i * delta_y);
        }
    }
    return grid;
}

void test1()
{
#if 1
    auto all_points = create_grid(10, 10, 2, 2);
    // insert 3 special points on 3 different raws
    all_points.emplace_back(3, 9);
    all_points.emplace_back(0, 2); // outside of the grid
    all_points.emplace_back(17, 13);
#elif 0
    auto all_points = create_grid(10, 10, 0, 0, 4, 4);
    // insert all 3 special points bewteen two adjacent points
    all_points.emplace_back(6, 5);
    all_points.emplace_back(6, 6);
    all_points.emplace_back(6, 7);
#endif
    std::vector<Point> special_points;
    find_points(all_points, special_points);
    for (const auto& p : special_points)
        std::cout << '(' << p.x_ << ',' << p.y_ << ")\n";
}

int main()
{
    test1();
    return 0;
}
