enum direction { NORTH, EAST, SOUTH, WEST };
enum wall { NORTH_WALL, SOUTH_WALL, WEST_WALL, EAST_WALL };

typedef struct {
	int x;
	int y;
	enum direction curr;
	int min_x;
	int max_x;
	int min_y;
	int max_y;
} traverser;

void walk(traverser* ptr);
void left(traverser* ptr);
void right(traverser* ptr);

