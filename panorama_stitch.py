import numpy as np
import cv2
import imutils

class panorama_image():
    def __init__(self):
        self.low_ratio = 0.85
        self.max_threshold = 5.0
        self.surf = cv2.xfeatures2d.SURF_create()

    def detect_feature_and_keypoint(self, image):
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # using SURF to detect features from the images
        (keypoints, features) = self.surf.detectAndCompute(gray, None)
        # convert list to ndarray
        keypoints = np.float32([i.pt for i in keypoints])

        return (keypoints, features)

    def get_all_match(self, features1, features2):
        # using euclit distance to compute all matches
        match_instance = cv2.DescriptorMatcher_create("BruteForce")
        all_matches = match_instance.knnMatch(features1, features2, 2)

        return all_matches

    def get_validmatches(self, allmatches):
        val_matches = []
        # find valid matches in all matches
        for val in allmatches:
            if len(val) == 2 and val[0].distance < val[1].distance * self.low_ratio:
                val_matches.append((val[0].trainIdx, val[0].queryIdx))

        return val_matches
    
    def match_keypoints(self, keypoint1, keypoint2, features1, features2):

        all_match = self.get_all_match(features1, features2)
        val_matches = self.get_validmatches(all_match)
        # computing homography between two sets of point least four matches
        if len(val_matches) > 4:
            # build the two sets points
            point1 = np.float32([keypoint1[i] for (_,i) in val_matches])
            point2 = np.float32([keypoint2[i] for (i,_) in val_matches])
            (homography, status) = cv2.findHomography(point1, point2, cv2.RANSAC, self.max_threshold)

            return (val_matches, homography, status)

    def warp_perspective(self, image1, image2, homography):
        valid = image1.shape[1] + image2.shape[1]
        # ward perspective for image1 to find result image 
        result = cv2.warpPerspective(image1, homography, (valid, image1.shape[0]))
        return result

    def images_stitching(self, images):

        (image2, image1) = images
        (keypoints1, features1) = self.detect_feature_and_keypoint(image1)
        (keypoints2, features2) = self.detect_feature_and_keypoint(image2)


        
        (matches, homography, status) = self.match_keypoints(keypoints1, keypoints2, features1, features2)
        result_image = self.warp_perspective(image1,image2,homography)
        result_image[0:image2.shape[0], 0:image2.shape[1]] = image2
        
        return result_image