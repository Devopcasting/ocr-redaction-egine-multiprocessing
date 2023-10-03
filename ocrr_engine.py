import multiprocessing
from watchdog.observers import Observer
from event_handlers.image_processing import ImageProcessingEnventHandler
from event_handlers.identify_card import IdentifyCard
from event_handlers.pan_card_p1_handler import PanCardPattern1Handler
from event_handlers.pan_card_p2_handler import PanCardPattern2Handler

# func: monitor the upload folder
def monitor_upload(monitor_upload_path):
    observer = Observer()
    image_processing_event_handler = ImageProcessingEnventHandler()
    observer.schedule(image_processing_event_handler, monitor_upload_path, recursive=True)
    observer.start()

    try:
        while True:
            observer.join()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

# func: monitor the processed images folder
def monitor_processed_image(monitor_processed_image_path):
    observer = Observer()
    identify_card_type_event_handler = IdentifyCard()
    observer.schedule(identify_card_type_event_handler, monitor_processed_image_path, recursive=True)
    observer.start()

    try:
        while True:
            observer.join()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

# func: monitor the pan card pattern 1 folder
def monitor_pan_card_p1(monitor_pan_card_p1_path):
    observer = Observer()
    pan_card_p1_event_handler = PanCardPattern1Handler()
    observer.schedule(pan_card_p1_event_handler, monitor_pan_card_p1_path, recursive=True)
    observer.start()

    try:
        while True:
            observer.join()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

# func: monitor the pan card pattern 2 folder
def monitor_pan_card_p2(monitor_pan_card_p2_path):
    observer = Observer()
    pan_card_p2_event_handler = PanCardPattern2Handler()
    observer.schedule(pan_card_p2_event_handler, monitor_pan_card_p2_path, recursive=True)
    observer.start()

    try:
        while True:
            observer.join()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()


# func: main
def main():
    # Create a process pool
    pool = multiprocessing.Pool()

    monitor_upload_process = pool.apply_async(monitor_upload, args=(monitor_upload_path,))
    monitor_processed_image_process = pool.apply_async(monitor_processed_image, args=(monitor_processed_image_path,))
    monitor_pan_card_p1_process = pool.apply_async(monitor_pan_card_p1, args=(monitor_pan_card_p1_path,))
    monitor_pan_card_p2_process = pool.apply_async(monitor_pan_card_p2, args=(monitor_pan_card_p2_path,))

    # Wait for all the process to finish
    pool.close()
    pool.join()

if __name__ == '__main__':

    # Directory path to monitor upload folder
    monitor_upload_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\upload'
    # Directory path to monitor the processed image folder
    monitor_processed_image_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\processed_images'
    # Directory path to monitor pan card pattern 1
    monitor_pan_card_p1_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\pan_card\pattern1'
    # Directory path to monitor pan card pattern 2
    monitor_pan_card_p2_path = r'C:\Users\pokhriyal\Desktop\Project-OCRR\images\pan_card\pattern2'


    # Run main
    main()