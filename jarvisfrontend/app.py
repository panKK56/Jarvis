from flask import Flask, request,render_template
import subprocess
import logging
app = Flask(__name__, static_folder='static',template_folder='templates')


# @app.route('/')
# def index():
#     return '''
#   <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Virtual Assistant Landing Page</title>
#     #<link rel="stylesheet" href="{{ url_for('static', filename='./static/jarvis.css') }}">
#     <link rel="stylesheet" href="./static/jarvis.css">
# </head>
# <body>
#     <div class="container">
#         <div class="main">
#         <header>
#             <ul class="navbar">
#                 <div class="st">
#                <a href="{{ url_for('static', filename='./templates/jarvisloginform.html') }}">Login</a> 
#                 <a href="jarvisoverview.html">Overview</a>
#                 <a href="./templates/jarvisfeatures.html">Feature</a>
#                 <a href="jarvisnavpoint.html">What is JARVIS ?</a>
#               </div>
#                 <p class="jarvis">JARVIS</p>
#                 <img src="./static/Marvel.jpg" alt="error" width="15%">

#             </ul>
            
#         </header>
#         <section id="features" class="features">
            
#             <div class="feature-item1">
#                 <div class="feature-icon">🎤</div>
#                 <h2 class="feature-title">Voice Commands</h2>
#                 <p class="feature-desc">Control your assistant with voice commands.</p>
#             </div>
#             <div class="feature-item2">
#                 <div class="feature-icon">📅</div>
#                 <h2 class="feature-title">Make PowerPoint Presentation</h2>
#                 <p class="feature-desc">Create and customize presentations with ease.</p>
#             </div>
#             <div class="feature-item3">
#                 <div class="feature-icon">💬</div>
#                 <h2 class="feature-title">Send Text Messages on WhatsApp</h2>
#                 <p class="feature-desc">Stay connected and send messages seamlessly.</p>
#             </div>
#             <div class="feature-item4">
#                 <div class="feature-icon">🔍</div>
#                 <h2 class="feature-title">Search Functionality</h2>
#                 <p class="feature-desc">Quickly find information using the search <br>feature.</p>
#             </div>
            
#         </section>
#     </div>
#    <div class="circle">
#        <form action="/run_python" method="post">
#         <input type="submit" value="Run Python File">
#     </form>
#     </div>


        
#       <div class="mn">
#         <section class="caro">
#             <div class="headerr">
#                 <h2> Don't take our word for it</h2>
#                  <p> Enhance Your Browsing: Get AI Suggestions, Translate, and Improve <br> Messages with GPT  While Freely Navigating the Web.</p>
#                </div>
#              <div class="carousel-container">
#                <button id="prevBtn" class="nav-btn">&lt;</button>
#                <div class="carousel">
#                  <div class="slide">
#                    I can't imagine my workday without Jarvis. It's like having a personal language assistant right in my browser. The translation function is seamless, the grammar correction is spot-on, and the instant response suggestions have turned me into a communication ninja. The AI tool also provides a new dimension of learning. It's a must-have!
#                    <p>Alex wong • Software Engineer</p> 
#                  </div>
#                  <div class="slide">
#                    Jarvis is a game-changer! As a frequent traveler, its quick translation feature has saved me countless times. The polished messaging tool ensures my emails are impeccable, and the smart replies are a time-saver. And don't even get me started on the AI insights—mind-blowing! Highly recommended for anyone looking to enhance productivity.
#                     <p> Jeff Mitchell • Marketing Specialist </p>
#                  </div>
#                  <div class="slide">
#                    Jarvis has simplified my interactions online. It's an all-in-one solution that delivers what it promises. The translation tool is impressively accurate, the message enhancement feature has made my communication more effective, and the smart replies are a real time-saver. The AI-powered knowledge tool is the cherry on top. Jarvis truly amplifies productivity!
#                      <p> Emily Johnson • Content Strategist</p>
                   
#                  </div> 
#                </div>
#                <button id="nextBtn" class="nav-btn">&gt;</button>
#                <button id="prevBtn" class="nav-btn">&lt;</button>
#              </div>
#              <script>
#              const carousel = document.querySelector('.carousel');
#              const slides = document.querySelectorAll('.slide');
#              const slideWidth = slides[0].clientWidth;
#              const prevBtn = document.getElementById('prevBtn');
#              const nextBtn = document.getElementById('nextBtn');
             
#              let counter = 1;
#              carousel.style.transform = `translateX(${-slideWidth * counter}px)`;
             
#              nextBtn.addEventListener('click', () => {
#                if (counter >= slides.length - 1) return;
#                counter++;
#                slideCarousel();
#              });
             
#              prevBtn.addEventListener('click', () => {
#                if (counter <= 0) return;
#                counter--;
#                slideCarousel();
#              });
             
#              function slideCarousel() {
#                carousel.style.transition = 'transform 0.5s ease-in-out';
#                carousel.style.transform = `translateX(${-slideWidth * counter}px)`;
#              }
             
#              function autoSlide() {
#                setInterval(() => {
#                  if (counter >= slides.length - 1) {
#                    counter = 0;
#                  } else {
#                    counter++;
#                  }
#                  slideCarousel();
#                }, 3000);
#              }
             
#              autoSlide();
#              </script>

#         </section>

#         <section class="getstart">
#             <div>
#               <h1>GET  STARTED</h1>
#               <p>Ready to experience the power of our virtual assistant?</p>
#               <a href ="./Template/jarvisloginform.html" class="cta-btn">Sign Up Now</a>
#             </div>
#           </section>
#         </div>
        

#           <div class="foot">
#             <footer class="footer">
#               <div class="ffp">
#               <img src="./static/Marvel.jpg" alt="error" width="35%">
#               <h5>Best AI Assistant Powered by GPT-4.5</h5>
#               <p class="desc">Experience a new level of efficiency and clarity with Jarvis. Seamlessly translate chats, perfect your messages, reply smartly, and tap into AI wisdom, all within a single application. Elevate your online interactions today.</p>
#             </div>
          
#                <div class="fsp"> 
#               <h3>PRODUCT</h3>
#               <ul>
#                 <li>Chat</li>
#                 <li>GPTs</li>
#                 <li>Reading and Writing</li>
#                 <li>AI Translator</li>
#                 <li>Grammar Checker</li>
#                 <li>Writing Improver</li>
#                 <li>Search Bar</li>
#                 <li>Code Review</li>
                
               
#               </ul>
#             </div>
          
#               <div class="ftp">  
#               <h3>EXPLORE</h3>
#               <ul>
#                 <li><a href="#">How it works?</a></li>
#                 <li><a href="#">Features</a></li>
#                 <li><a href="#">Privacy</a></li>
#               </ul>
#             </div>
          
#               <div class="ffrp">  
#               <h3>CONTACT</h3> 
#               <ul>
#                 <li><a href="#">Facebook</a><br>
#                   <img src="./static/Facebooklogo.png" alt="error" width="2%">
#                 </li>
#                 <li><a href="#">Twitter (X)</a> <br>
#                   <img src="./static/twitterlogo.png" alt="error" width="2%">
#                 </li> 
#                 <li><a href="#">Linkedin</a><br>
#                   <img src="./static/LinkedInlogo.png" alt="error" width="2%">
#                 </li>
#                 <li>Email: <a href="mailto:hello@jarvis.cx">hello@jarvis.cx</a><br>
#                   <img src="./static/email.logo.png" alt="error" width="2%">
#                 </li>
#               </ul>
#             </div>
            
              
#           </footer>
#           <p class="copyr">&copy; 2024 Virtual Assistant. All rights reserved.</p>
          
#             </div>
#     </div>
# </body>
# </html>


#     '''
@app.route('/')
def index():
    return render_template('jarvis.html')

@app.route('/login')
def login():
    return render_template('jarvisloginform.html')

@app.route('/overview')
def overview():
    return render_template('jarvisoverview.html')

@app.route('/features')
def features():
    return render_template('jarvisfeatures.html')

@app.route('/navpoint')
def navpoint():
    return render_template('jarvisnavpoint.html')
@app.route('/run_python')
def run_python():
      subprocess.run(['python', "C:\Jarvis\main.py"])  # Adjust path if needed
      return render_template('jarvis.html')
   

if __name__ == '__main__':
    app.run(debug=True)