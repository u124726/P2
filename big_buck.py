import subprocess
import cv2


# EXERCISE 1
def mp4_to_mpeg(mp4_input, mpeg_output):
    """ Translate Big Buck Bunny video from .mp4 format to .MPEG and shows video metadata using ffmpeg
     Args:
            mp4_input: .mp4 video to be converted
            mpeg_output: .mpeg output video
    """
    ffmpeg_mp4_to_mpeg = [
        'ffmpeg',
        '-i', mp4_input,
        mpeg_output
    ]
    subprocess.run(ffmpeg_mp4_to_mpeg)

    ffmpeg_video_info = [
        'ffprobe',
        '-show_streams',
        '-show_format',
        mpeg_output
    ]
    subprocess.run(ffmpeg_video_info)


# mp4_to_mpeg('big_buck_bunny.mp4', '/mnt/c/Users/dcabo/PycharmProjects/P2Video/bb_output.mpeg')


# EXERCISE 2
def resolution(input_video, output_video, input_width, input_height):
    """ Changes video resolution from input video using ffmpeg
     Args:
            input_video: video to be converted
            output_video: output video with new resolution
            input_width: width of new output video
            input_height: height of new output video
    """
    ffmpeg_resolution = [
        'ffmpeg',
        '-i', input_video,
        '-vf', f'scale={input_width}:{input_height}',
        output_video
    ]
    subprocess.run(ffmpeg_resolution)


# resolution('big_buck_bunny.mp4', '/mnt/c/Users/dcabo/PycharmProjects/P2Video/bb_resolution.mp4', 960, 540)


# EXERCISE 3
def chroma_subsampling(input_video, output_video):
    """ Perform video chroma_subsampling with 8-bit 4:2:0 format using ffmpeg
     Args:
            input_video: video to be converted
            output_video: output video with new resolution
    """
    ffmpeg_chroma = [
        'ffmpeg',
        '-i', input_video,
        '-vf', f'format=yuv420p',
        output_video
    ]
    subprocess.run(ffmpeg_chroma)


# chroma_subsampling('big_buck_bunny.mp4', '/mnt/c/Users/dcabo/PycharmProjects/P2Video/bb_ch_sub.mp4')


# EXERCISE 4
def read_print_info(input_video):
    """ Read video info and print 5 relevant data of it
     Args:
            input_video: video to be read
    """
    video_data = cv2.VideoCapture('big_buck_bunny.mp4')
    height = video_data.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = video_data.get(cv2.CAP_PROP_FRAME_WIDTH)
    n_frames = video_data.get(cv2.CAP_PROP_FRAME_COUNT)
    frames_per_sec = video_data.get(cv2.CAP_PROP_FPS)
    format_ = video_data.get(cv2.CAP_PROP_FORMAT)
    frames_type = video_data.get(cv2.CAP_PROP_FRAME_TYPE)
    duration = n_frames / frames_per_sec

    print("Video info obtained for our input video is the following:")
    print("Video Dimension: height:{} width:{}".format(height, width))
    print("Number of frames:" + str(n_frames))
    print("Number of frames per second:" + str(frames_per_sec))
    print("Format:" + str(format_))
    print("Type:" + str(frames_type))
    print("Duration:" + str(duration))


# read_print_info('big_buck_bunny.mp4')


# EXERCISE 5
def resize_and_bw(video_input, video_output, bwvideo_output, input_width, input_height):
    """ Resize Big Buck Bunny video into high lower quality (from 100% dimension to 10%) reducing it from 100% to 5% and change the results to grayscale using ffmpeg
        Args:
            video_input: Video to be converted
            video_output: New video resized
            bwvideo_output: New video in grayscale
            input_width: Width of resized
            input_height: Image to be resized
    """
    ffmpeg_resize = [
        'ffmpeg',
        '-i', video_input,
        '-vf', f'scale={input_width}:{input_height}',
        video_output
    ]

    ffmpeg_bw = [
        'ffmpeg',
        '-i', video_output,
        '-vf', f'format=gray',
        bwvideo_output
    ]
    subprocess.run(ffmpeg_resize)
    subprocess.run(ffmpeg_bw)


resize_and_bw('big_buck_bunny.mp4', '/mnt/c/Users/dcabo/PycharmProjects/P2Video/bb_lower_quality.mp4', '/mnt/c/Users/dcabo/PycharmProjects/P2Video/bb_bw.mp4', 182, 72)

"""MP4 tiene un alto nivel de compresión por lo que hemos decidido reducir en un 90% el tamaño original de nuestro vídeo, 
en este caso de dimensiones 1280x720 a dimensiones 128x72. Podemos observar en los resultados como hay una pérdida muy 
significativa en la calidad de nuestro vídeo a la vez que una reducción en el tamaño de nuestro archivo, de 10.3Mb a 1.36Mb;
también podemos observar entre el posterior vídeo en escala de grises como existe una ligera reducción en el tamaño del 
archivo, en este caso de 1.36Mb a 1.28Mb, lo cual nos indica una ventaja de los vídeos en escala de grises respcto de los
de color en términos de compresión."""

