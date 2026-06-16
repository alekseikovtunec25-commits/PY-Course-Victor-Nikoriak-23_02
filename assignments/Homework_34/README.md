Task 1

A shared counter

Make a class called Counter, and make it a subclass of the Thread class in the Threading module. Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000. Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times) and for each time increments the value of the counter by 1. Create 2 instances of the thread and start them, then join them and check the result of the counter, it should be 200.000, right? Run it a couple of times and consider some different reasons why you get the answer that you get. 

 

Task 2

Echo server with threading

Create a socket echo server which handles each connection in a separate Thread

 

Task 3

Requests using multithreading

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 

As a result, store all comments in chronological order in JSON and dump it to a file. For this task use Threads for making requests to reddit API.