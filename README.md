# Live Desktop
The goal is to have a video as your desktop background. Right now I am working on extracting the frames from the video and perfecting the algorithm.

There are few bugs in the program at the moment. Here is a list of bugs that needs fixing:

 * When extracting frames from a video, It takes 1 hour to extract all the frames from a 4 minute video. So imagine a 8 minute video.

 * The method used to find the number of frames does not work that great. Method is the duration in milliseconds x FPS. If a video is 60 FPS and is 8 minutes (490000 milliseconds) long that would equal 29,400,000 frames that would be 36 hours and 6 minutes. 

If you are intrested in the project consider modifying the code and opening a pull request.
