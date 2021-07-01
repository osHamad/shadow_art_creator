from shadow_art import Shadow
myshadow = Shadow('video.mp4')
myshadow.make_shadow_frames(binary_thresh1=225, binary_thresh2=255)
myshadow.frames_to_video('output.mp4')
