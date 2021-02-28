FROM python:3.8.5-alpine
# Create and set the work directory inside the image named 'app'
WORKDIR /app
# Execute a pip install command using the list 'requirements.txt'
COPY . .
# Copy the app file into the image working directory
RUN pip install -r requirements.txt
# State the listening port for the container. 
# The app's code does not actually specify the port, so it would be useful to include here.
EXPOSE 5001
# Run 'python app.py' on container start-up. This is the main process.
ENTRYPOINT ["python", "app.py"]
