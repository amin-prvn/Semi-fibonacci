# Sheypoor Task
First element must be 0 and second one, 1 , Each of the next elements is equal to the sum of the digits of the previous two elements.

Sample of this sequence:
```
0, 1, 1, 2, 3, 5, 8, 13, 12, 7, 10, 8, 9,...
```
### Big(O)
The time complexity of this fuction is O(n * k) = O(n)

### Space Complexity
O(1)

## How run unit test
To build the unit-test Docker image:
```
docker build -t test-sequence-image -f DockerfileTest .
```
To run the unit-test Docker container:
```
docker run --rm test-sequence-image
```
## How run sequence code
To build the Docker image:
```
docker build -t sequence-image -f Dockerfile .
```
To run the Docker container:
```
docker run --rm sequence-image
```