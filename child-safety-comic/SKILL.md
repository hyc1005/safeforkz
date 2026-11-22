---
name: child-safety-comic
description: Help a caregiver choose what to teach, then create a wordless side-by-side safety comic for a young child. Use for everyday safety scenes such as stairs, playgrounds, kitchens, and roads, or when the caregiver wants a portable image prompt.
---

# Child Safety Comic

Default to ages 3 to 6 and one everyday safety lesson per image. Talk to the caregiver in their language. Write image prompts in English.

## Confirm the teaching intent

1. Identify the setting, risky action, safer action the child can perform, and possible direct consequence. Reuse details already given. If a safety premise is uncertain, consult authoritative guidance when available. Briefly correct unsupported claims and offer a supported teaching goal.
2. Ask one question at a time when the answer will change the picture. Offer two or three concrete options, accept free-form replies, and wait. For a broad request, offer settings first. For a named setting such as a slide, offer distinct lessons such as waiting for the exit to clear, sliding seated with feet first, or clearing the exit after landing.
3. Once the lesson is clear, settle the possible left outcome and the safer right ending before choosing the grid. Use any outcome the caregiver already specified. When the endpoint is unclear, offer short storyboard choices such as recovering before contact, showing contact, or showing the reaction afterward. Work backward from both endings to the visible actions needed to explain them. Show the exact panel count, left outcome, and right ending in each option. If the caregiver supplied a complete storyboard, summarize it for approval instead. A selection that completes the storyboard, or an explicit instruction to draw the complete storyboard, counts as approval. Apply edits supplied with the selection and ask again only if a material ambiguity remains.

## Write the approved image prompt

Provide one portrait comic with exactly two columns. Default to three rows: the shared starting situation, the action that changes each path, and each visible outcome. Add a fourth row when two essential moments need separate pictures, such as contact followed by the child's reaction. Pair comparable moments across columns and read each column top to bottom. If the caregiver explicitly requests four panels, explain which beats can be combined and let them choose a shorter version or six panels when the full story needs more room.

Start each standalone English prompt with a single resolved layout: give the total number of equal rectangular panels, two equal columns, the exact row count, one full-height white vertical gutter, and the exact number of full-width white horizontal gutters. Describe every position once as top or numbered row, left or right, with one main action per cell. These locations are composition instructions. All selection numbers, dialogue, and caregiver guidance stay in the conversation.

Include these constraints in every prompt:

- Completely wordless artwork. Render no letters, numbers, pseudo-writing, labels, captions, balloons, sound effects, logos, arrows, checkmarks, or explanatory icons. Use blank book covers, clothing, packages, and signs. Include only people, their actions, relevant objects, and the surroundings needed to read those actions.
- Original preschool characters with round faces, clean outlines and flat colors. All open eyes show a distinct white sclera, a dark iris and a smaller black pupil. Direct the gaze toward the object or person that matters. Use naturally closed eyes when the action calls for it.
- Keep each character, outfit, setting, and object consistent. Show natural arms and hands, with an unambiguous owner and visible contact where it matters. A matched close view can clarify a tiny contact such as fingertips in a door gap. Use the same view for the corresponding safe action.
- Show the direct possible consequence of the risky action. If the caregiver selected an actual accident, show the contact or loss of support and what follows. A recoil, flinch, loss of balance, or tears can fit the event. Keep the depiction non-graphic, with no blood, visible wounds, limb distortion, severe impact close-ups, scolding, or humiliation. A simulated near miss ends before contact.
- Give the safer action a plausible ending. Use visible landmarks to establish movement and relative positions. Carry the previous panel's movement through to where characters and objects end up. When changing views, keep a recognizable landmark in frame. When asking for help fits, let the child look at the adult, gesture and open their mouth, then show the adult responding. Caregivers supply the narration.

## Deliver and check

- When image generation is available, use the approved final prompt to produce the image. When the caregiver requests a prompt or the session can only produce text, return the final prompt as one copyable English code block. If the caregiver wants another conversational tool to run the whole workflow, provide [the interactive prompt](references/interactive-prompt.txt). A prompt-only image interface receives the final drawing prompt after the choices have been made.
- At about 360 pixels wide, inspect the exact grid and wordlessness. Read each column on its own and identify what the child wanted, which action changed the outcome, and where the people and objects ended up. Check that the last panel follows the approved outcome and the visible movement. At full size inspect lettering, white sclera in open eyes, character continuity, hands and fingers, contact points, and non-graphic content.
- If a specific panel fails, name its position and correct the visible defect. Incorrect row counts, merged panels, or words call for a full prompt retry. If the model still drops rows, generate one matching left/right pair per row and stack the pairs top to bottom using equal heights and white gutters. Review the assembled image. When a tool cannot display the output, ask the caregiver to share it for inspection before calling it verified.
- Deliver the checked comic. Offer a short narration line outside the artwork if requested.

## Storyboard examples

- **Stairs, six panels.** Establish the downhill direction with a side view of descending treads. Left shows descent with hands in pockets, a missed tread with a forward fall, then cheek-to-floor contact at the foot of the stairs. Right shows the child grasping the railing, stepping down while holding it, then standing with both feet on the landing.
- **High book, six panels.** Left shows a child climbing a stool, the stool tipping, and the child sitting on the floor holding a knee. Right shows the child staying on the floor, pointing at the book and looking toward an adult who retrieves and hands over that same unlettered book.
- **Ball at the curb, eight panels.** Start with a ball rolling off the curb. On the left the child follows it, a car makes simplified side contact and the child loses balance, then the caregiver comes to the seated child. On the right the child stops on the sidewalk and calls the caregiver. The two hold hands while the car passes left to right, ending with its rear leaving the right edge.
- **Hot pot, six panels.** Show the adult washing vegetables side-on and initially looking at the sink. For a near miss, the child reaches toward the hot handle, pulls back with a visible gap between finger and handle, then steps away. If the approved ending includes touching the handle, show contact before the recoil. On the right the child stays back, calls the adult, and waits at the table while the adult tends the pot.
- **Door gap, six panels.** The adult operates the door. On the left the child reaches into the open gap, the edges close around the fingertips, and the child withdraws the sore hand when the door opens. On the right the child steps back with hands at the chest while the adult closes the door. Match the closer views of the gap.
- **Slide exit, six panels.** Both columns begin with one child seated at the top and another at the exit. On the left the first child slides too soon, and their shoulders touch as one loses balance. On the right the first child waits until the exit is clear, then slides seated with feet first. Use those actions when a caregiver suggests an unsupported rule such as crossing the feet to prevent fractures. [American Academy of Pediatrics playground guidance](https://www.healthychildren.org/english/safety-prevention/at-play/pages/safety-on-the-playground.aspx)
