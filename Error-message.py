---------------------------------------------------------------------------
error                                     Traceback (most recent call last)
<ipython-input-27-7791191b7584> in <module>
      2   return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      3 
----> 4 data['pixels'] = data['pixels'].apply(grayscale)

4 frames
<ipython-input-27-7791191b7584> in grayscale(image)
      1 def grayscale(image):
----> 2   return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      3 
      4 data['pixels'] = data['pixels'].apply(grayscale)

error: OpenCV(4.6.0) /io/opencv/modules/imgproc/src/color.simd_helpers.hpp:92: error: (-2:Unspecified error) in function 'cv::impl::{anonymous}::CvtHelper<VScn, VDcn, VDepth, sizePolicy>::CvtHelper(cv::InputArray, cv::OutputArray, int) [with VScn = cv::impl::{anonymous}::Set<3, 4>; VDcn = cv::impl::{anonymous}::Set<1>; VDepth = cv::impl::{anonymous}::Set<0, 2, 5>; cv::impl::{anonymous}::SizePolicy sizePolicy = cv::impl::<unnamed>::NONE; cv::InputArray = const cv::_InputArray&; cv::OutputArray = const cv::_OutputArray&]'
> Invalid number of channels in input image:
>     'VScn::contains(scn)'
> where
>     'scn' is 1
