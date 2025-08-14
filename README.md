# quick-culvert-sizer

quick-culvert-sizer is intended for a user with a background in civil engineering, especially for those in a drainage and/or infrastructure. For others, this may only be a curious novelty.

In the civil engineering consulting sector, chasing new projects with proposals is routine. In this phase, the team needs to put together a preliminary design for the tender process of a RFP(Request for Proposal) and sub
mit a preliminary cost estimate as a part of this. At this stage, project engineers will need to create a drainage area map from contour maps which can take a few days. As part of this, a diligent civil engineer will analyse and comupute the time-of-concentration (Tc) for each drainage area. The time-of-concentration is the time in minutes for a raindrop to travel, from the most remote point and most likely path, to the point of intereset. With quick-culvert-sizer and once the time-of-concentration's are known (generally a few days) the user can use the results of this app to quickly select a reasonable design. No more "seat-of-the-pants" risky guessing. 

Incorrectly sizing a box culvert can lead to costly errors in the preliminary cost estimate (i.e. $250,000 vs maybe $50,000). Using this app, the user can get a "worst-case" but accurate design of the box-culvert required (if any). If the project proposal was successful (i.e. new project budget has been won), the engineering team can go to detailed design with much more effort and using quick-culvert-sizer results as a starting point. During detailed design, there should be no nasty surprises and the box-culvert size can only be smaller (i.e. cheaper). Also, phsical constraints can be managed and since if this is a roadway project and culvert geometry for roadway projects are the driving factor of vertical roadway alignment geometry. In turn, the vertical roadway geometry is the driver for earthwork (i.e. cut and fill quantities) which can be extremely expensive and cause a project to lose a lot of money.

Here is a flowchart of the process:

![Alt text](images/flowhart.png)



## Features 

Command line driven app that accetps user input for a catchment area and runs up to 490 iterations to calculate the best box culvert design options and outputs to terminal.

## Testing 

### User input
  - __Input Catchment Area Size__

      ![Alt text](images/input_catchment_area.png)

  - __Input Catchment Area Incorrect__

      ![Alt text](images/input_catchment_area_incorrect.png)

  - __Input Catchment Area Correct__

      ![Alt text](images/input_catchment_area_correct.png)

  - __Input Catchment Area Relief Incorreect__

      ![Alt text](images/input_catchment_area_relief_incorrect.png)

  - __Input Catchment Area Relief__

      ![Alt text](images/input_catchment_area_relief.png)

  - __Input Catchment Area Soil Infiltration__

      ![Alt text](images/input_catchment_area_soil_infiltration.png)

  - __Input Catchment Area Soil Infiltration Incorrect__

      ![Alt text](images/input_catchment_area_soil_infiltration_incorrect.png)

  - __Input Catchment Area Soil Infiltration Correct__
      ![Alt text](images/input_catchment_area_soil_infiltration_correct.png)

  - __Input Catchment Area Soil Vegetation Cover Incorrect__
      ![Alt text](images/input_catchment_area_vegetation_incorrect.png)

  - __Input Catchment Area Soil Vegetation Cover Correct__
      ![Alt text](images/input_catchment_area_vegetation_correct.png)

  - __Input Catchment Area Surface Storaage Incorrect__
      ![Alt text](images/input_catchment_area_surface_storage_incorrect.png)

  - __Input Catchment Area Surface Storaage Correct__
      ![Alt text](images/input_catchment_area_surface_storage_correct.png)

  - __Input Assumed Flow Velocity Incorrect__
      ![Alt text](images/input_assumed_flow_velocity_incorrect.png)

  - __Input Assumed Flow Velocity Correct__
      ![Alt text](images/input_assumed_flow_velocity_correct.png)

  - __Input Maximum Box Height__
      ![Alt text](images/input_max_box_height.png)


  - __Input Maximum Box Height Incorrect__
      ![Alt text](images/input_max_box_height_incorrect.png)

  - __Input Maximum Box Height Incorrect Repeat = No__
      ![Alt text](images/input_max_box_height_correct_repeat_no.png)

  - __Results Repeat = Yes__
      ![Alt text](images/repeat_app_yes.png)

  - __Results Repeat = No__
      ![Alt text](images/repeat_app_no.png)

  - __Expected Results__

      Since there can be hundreds of iteration it is only feasible to take a random iteration
      and compare it to an Excel solution for that iteration. A random iteration sample gives
      the results expected.

      ![Alt text](images/_expected_results.png)


### Validator Testing 

- Flake8
  - No significant errors according to Flake8 Linting. A number of 'line too long' messages. Doing research on Google, this seems to be a legacy message from the past which is no longer relevant today.


### Unfixed Bugs

Haven't noticed any bugs.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html

- If not available register and sign up for a Heroku account
- From dashboard click "Create New App" and enter name of app

    ![Alt text](images/Heroko_dashboard_create_new_app.png)

- Name the app, select region, click "Create app"

    ![Alt text](images/Heroko_create_app.png)

- Name the app, select region, click "Create app"

    ![Alt text](images/Heroko_connect_app_to_github_repository.png)

- Click Github, search for your Github repository

    ![Alt text](images/Heroko_connect_app_to_github_repository.png)

- Using this already deployed app as an example, on the dashboard click on "Settings" and navigate  to "Buildpacks and add these items in this order while clicking "Add buildpack".

    ![Alt text](images/Heroko_settings_buildpacks.png)

- By now you should be connected to Github, select "Deploy" from dashboard, and then click "Deploy branch" from "Manual deploy" section

    ![Alt text](images/Heroko_deploy_app.png)

- Once successfully deployed, open app in browser terminal

    ![Alt text](images/Heroku_once_deployed_open_app.png)

    ![Alt text](images/Heroku_running_app.png)


## Credits 

Texas Department of Transportation - Hydraulic Design Manual
NOAA National Weather Service https://hdsc.nws.noaa.gov/pfds/
Code Institute

### Content 

- Readme from Love Sandwiches was used as template

### Media

None 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 





