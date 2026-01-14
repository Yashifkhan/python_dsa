print("simple youtub project")

import json

def load_videos():
    try:
        with open('youtube.text','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtub.text','w') as file
    json.dump(videos,file)

def delete_video(videos):
    return "delet the video"

def update_video():
    return "update the viode deatils"

def add_video():
    return "add video"

def list_all_video():
    return "all videos get"

def main():
    videos=load_videos()
    while True:
        print("\n youtube manager || choose an option")
        print('1. List all youtube videos')
        print('2. Add new video')
        print('3. update video details')
        print('4. delete a video')
        print('5. exit a app')

        choice=input("Enter choice : ")

        match choice:
        case '1':
            list_all_video(videos)
        case '2':
            add_video(videos)
        case '3':
            update_video(videos)
        case '4':
            delete_video(videos)
        case '5':
            break
        case _:
            print('invalid choice')

if __name__ == "__main__":
    main()