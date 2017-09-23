09/23/17

Create new project:
-  go to ~/_posts/ create new file with specified format
-  attach html content from the project and add header such as (example from 2017-05-05-smartcar.html)

'''
---
layout: project
title: Train a Self-driving Car Using Reinforcement Learning
date: 2017-05-05 09:00:00

categories: project
description: The reinforcement learning technique was applied for a self-driving agent in a simplified world to aid it in effectively reaching its destinations in the allotted time.
---
'''

-  edit the title, date, and description
-  edit ~/project.html for adding content into project page

'''
        <div class="col-xs-5">
             <a href="{{ "/project/2017/05/12/dlnd_image_classification.html" | prepend: site.baseurl }}">
             <div class="authorimage box" style="background: url({{site.baseurl}}/assets/img/project_image_classification_deep.jpg);
             width: {{page.fig_width}}; height: {{page.fig_height}};"> </div> 
               <div style='width: {{page.caption_width}};   text-align: center; color: black;'>Classify the Image</div>
             </a>
        </div>
'''

-  change the href link, change the displayed image, and the title of the project