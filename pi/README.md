<!-- ABOUT THE PROJECT -->
## Raspberry PI DAQ for SAHT ENERGY

<!-- GETTING STARTED -->
## Getting Started

Follow the Prerequisites and the read the Usage setting to get started.

### Prerequisites


* gpiozero
  ```sh
  pip install gpiozero
  ```

* pandas
  ```sh
  pip install pandas
  ```

* matplotlib
  ```sh
  pip install matplotlib
  ```

* tkinter
  ```sh
  pip install tkinter
  ```

### Installation

1. Follow the setup instructions for the DAQ hat at  [https://github.com/mccdaq/daqhats](https://github.com/mccdaq/daqhats)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The Raspberry PI is ran using simple python scripts to monitor the state of temprature, water, voltage, current, and encoder sensors and convert and display the data in real time. Once the Installation process is fully complete the user can then simply run the final.py script on the Raspberry PI and the script will automatically display and log data into data.csv file in the local folder. When you wish to stop loggin and visulizing data simply close the display window. The data can then be exported via the usb port to a computer and viewed in excel or any other program. 

Right now only the MarineEnergyBasic.py code works as it there was a problem implenting the previous solution with multiple python threads and a work around is being thought of to display this data visually over time. 



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Marshall Bluhm - mabluhm71@comcast.net

Dr. Craig Hill - cshill@d.umn.edu

Project Link: [https://github.com/hillcraig//Benchtop_PTO_MarineEnergy](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Dr. Craig Hill
* Den Ramsey
* Marshall Bluhm
* Grant Koeler
* Dakota Benigni
* Nick Klaustermeier
* Ethan De Jesus

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
