## Vehicle-Data-Encoder-Decoder

# Objectives
Learn how to:

* use the json module and its basic facilities;
* encode and decode JSON strings from/to Python objects.

# Scenario

Take a look at these two screenshots. They present two different use cases of the same program:
![3830113a00e2f2f9ebf9cb037bb12b34ac3d842c](https://github.com/user-attachments/assets/5f40eec2-6116-4f24-82af-e1f9035c8f44)

The task is to write a code which has exactly the same conversation with the user and:
![2dd348358deaed7a48e03730fec2e242990d0a24](https://github.com/user-attachments/assets/a4ade020-8df1-4671-b4c8-d8a37b9d3331)

1. defines a class named Vehicle, whose objects can carry the vehicle data shown above (the structure of the class should be deducted from the above dialog — call it "reverse engineering" if you want)
2. defines a class able to encode the Vehicle object into an equivalent JSON string;
3. defines a class able to decode the JSON string into the newly created Vehicle object.

Of course, some basic data validity checks should be done, too. We're sure you're careful enough to protect your code from reckless users.

