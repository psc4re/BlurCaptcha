BlurCaptcha
===========
Considering the growing sophisticated attack technologies and threat of the 3rd party human attacks on existing CAPTCHA technologies, the industry is in need of a reliable, easy and more secure technique. This section describes our proposed method of Blur CAPTCHA which not only generates the simplest images of text CAPTCHA making it highly readable for human users defending against automated attacks and using a time based method to counter the 3rd party human attack. 

A.	Blur CAPTCHA Concept and Implementation:

Blur CAPTCHA uses a technique of blurring the background of the image into a thin character such that the density of the color converges into a thin line of single pixel to form the character. The figure x shows the example of Blur CAPTCHA where the background is blurred to generate the CAPTCHA characters. 

 
Figure x

A PHP script is used to generate the background image and then based on the text required to generate the CAPTCHA the background image is blurred either to converge or diverge the density of color to display the characters as thin as a pixel making it easy for the users to read the characters however difficult to automated scripts as the pixel density of the characters almost matches with the background pixel density. The background image is also made to contain some other characters and shapes around the image but displayed in high or contrasting color or in small sizes or extremely large size to separate it from the original CAPTCHA text. 
 
Figure x showing the convergence of pixel density

 


Figure showing the divergence of color until single pixel

Another step would be to include a dynamic set of input boxes. The PHP script generates a dynamic set of input boxes and the user in asked to input the CAPTCHA solution only in a particular one input box. The CAPTCHA fails if the user inputs the solution wrong or in a wrong input box. The script can generate any number of input boxes in any order, using random IDs for the textbox inputs, there by tricking the automated scripts. The user is only expected to enter the correct CAPTCHA test in the input box as suggested by the CAPTCHA. Figure shows the input boxes of the CAPTCHA. 
 
Figure 

B.	Security Features:

As previously discussed our concern for security is mostly due to the developing image processing techniques and threat from 3rd party based human attacks. Most current CAPTCHA implementation techniques use a timeout value for their CAPTCHA; however the time required for delivering the CAPTCHA image to 3rd party human solver is very less and therefore there is not enough trust established to confirm that the response was from a legitimate user or an attacker. 
To solve this problem we can use a neural network based timeout technique which predicts the time required for a legitimate user to solve the CAPTCHA and generate the timeout value based on the predicted time. This technique can be evolve over time to predict more accurate time out values to curb the 3rd party human attackers by not providing enough time for transmission of CAPTCHA image among the attackers.   
Techniques like source code padding, disabling the right clicks within the container of the CAPTCHA, and encrypting the CAPTCHA JavaScript can be used to hide the source code and URLs of the CAPTCHA resources. 
