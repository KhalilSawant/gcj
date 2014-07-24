#ifndef __POINT_H__
#define __POINT_H__

class Point {
	private:
		int x;
		int y;
	public:
		void setX(int x) { this->x = x; }
		void setY(int y) { this->y = y; }
		int getX() { return x; }
		int getY() { return y; }

		bool equals(const Point& other);
		unsigned int distanceSquared(const Point& other);
		double slope(const Point& other);
};	

#endif
