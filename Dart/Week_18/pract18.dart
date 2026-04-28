void main() {
  Car mycar = Car('red', 60);
  print(mycar);
  print(mycar.distance(1));
}

class Car {
  String colour;
  double speed;

  Car(this.colour, this.speed);

  void accelerate(double inc) {
    speed += inc;
  }

  void brake() {
    speed = 0;
  }

  double distance(double time) {
    return speed * time;
  }

  String toString() {
    return 'Car(colour: $colour, speed: $speed)';
  }
}
