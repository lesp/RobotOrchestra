# Project 1 - Scratch Drums  

Instruments can be made from anything, and in this project we shall build a drum kit out of arts and crafts materials.

  
For this project you will need  

* A Raspberry Pi  
* 3 x Plastic Cups  
* Aluminium foil
* Cellotape
* Wire strippers
* 2 x Pencils or chopsticks
* Breadboard  
* A selection of male to female and male to male wire  
* A speaker or monitor with audio  
* The latest version of Raspbian operating system

We shall start by setting up the drums. Take a length of aluminium foil and wrap it tightly over a plastic cup. Now take a male to female wire and chop off the male end. Using the wire strippers strip approximately 3 centimetres of the sheath to show exposed wire.

Using cellotape, affix the exposed wire to the aluminium foil, ensure a good contact between them and secure a short length of wire to the cup for strain relief.

Repeat this process two more times so that you have three "drums"

Now we shall use a similar technique to make two "drumsticks", which will use aluminium foil as their "heads" and exposed wires used to connect the drumsticks to the Raspberry Pi.

For the drums and drumsticks we will now need to link together a series of male to female wires. The length should be plenty to use the drums, but not enough to get tangled up.

Connect the drums to GPIO pins 2,3,4\.

Connect the drumsticks to Ground (GND)

Attach the accessories for your Raspberry Pi and power up to the desktop.

From the main menu click on Programming, and then look for Scratch in the sub menu. Open Scratch.

## What is Scratch?

Scratch is a block based programming environment that focusses on experimentation and enables non coders to quickly build projects.

Blocks are contained in groups which are located on the left of the screen. The main coding area is in the centre, and the stage, where actions and outputs can be seen, is on the right.

To write code we drag blocks from the left and into the centre of the screen, joining them together to form sequences.

## Creating our code.  

Our first block of code is called "When Green Flag Clicked" and this can be found in the Control group. This is called a "Hat Block" and it serves as event, meaning that when the Green Flag icon is clicked the code will start.

Our next block of code is a Broadcast and this is also in the Control group. Drag four Broadcast blocks and connect them together, one atop the other. Now link these to the Hat Block.

For the first Broadcast, click on the black arrow to the right of the block. Click on New/Edit and type the following

*gpioserveron*

Click on Ok to save.

For the second Broadcast click on the black arrow and then New/Edit. Enter the following.

*config2input*

Click on Ok to save.

Repeat this process for the next two Broadcast blocks changing them to

*config3input*

*config4input*

Our next block is also inside the Control group and it is called "Forever", this is a loop and as the name suggests it will carry on forever. Drag the forever loop from the left and attach it underneath the code that we have just created.

Inside of the forever loop we shall now drag three "If" conditionals, these are also in the Control group. Stack the "If" blocks on top of each other. So now we have a loop that will look to see if any of the three If conditions are true. 

In the Operators group, look for the block that read " \_\_ = \_\_ ", drag this into the hexagon shape that is present on the If block.

Look for the Sensing group, coloured Blue. Click on the group and look for a block that reads "slider sensor value" click on the drop down arrow and select*gpio2* from the list. Drag this block to first space present on the "\_\_=\_\_" Operator block.

In the remaining blank space of the "\_\_=\_\_" Operator block type a zero.

Repeat this process for gpio3 and gpio4 and place their block inside the two remaining If conditions. Each If condition will contain the blocks for only one gpio pin, so our first contains *gpio2*, second contains *gpio3* and the final If condition contains the code for *gpio4*.

With the conditions written, we shall write the code that will run once the conditions are met. For each of the If conditions we shall play a drum sound.  

In the Sound group look for "Play Sound meow" drag this block and place it inside the If condition. Just above the coding area there are three tabs, currently we are in Scripts, click on Sounds. You will now see that we have the meow sound listed. To load another sound click on Import and select any sound that you wish. We chose a drum / percussion instrument. When a sound is loaded it is added to a list. We can now go back to our code by clicking on the Scripts tab. Change the sound that is played by clicking on the drop down arrow of the "Play Sound" block. 

Repeat these steps for the two remaining If conditions.

We have now written the code the project, remember to save your work before progressing further.

To start the project, click on the Green Flag icon in the top right of the screen. Now pick up your drumsticks and start drumming!