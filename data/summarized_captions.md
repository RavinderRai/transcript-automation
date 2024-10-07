## Category: engineering

### Video ID: rOqgRiNMVqg

# Youtube Transcript Text
So it is the Security, Governance, Growth, and Data Science Meeting applied ML, ML Ops, and an anti-abuse team meeting. This is our meeting for September 14th or 15th in APAC.

The anti-abuse is moving product sections from security to data science. Data science is effectively a rename of the Model Ops section. Data science will include two stages: the existing Model Ops, which has three groups in it that one can talk more about, and the Anti-Abuse stage, which only currently has one group called Anti-Abuse. I think at some point there are plans to split Anti-Abuse into two groups, but that's not in the near future, and we're working through all the changes around that.

Regarding the big rocks and hot issues section, we've implemented like a weekly refinement meeting kind of checking to make sure that stories are broken down tiny enough. I think with smaller bits of work, we're seeing a higher MR rate. It's debatable whether or not that's just inflated, right, like you can work on a small piece of code and ship it and you can do that a lot of times, you're going to get a higher MR rate. We're trying to be reasonable with that. I am noticing a nice tick up after implementing the refinement meeting, so let's hope for the best.

A note on refinement in stack analysis: We're experimenting with a new section in our planning feature called 'looking forward,' and in there, we're using that as a baseline where we add issues that we think need refinement that will most likely be worked on in the next one to three milestones.

Okay, after that, the all right bed ramp and the can't or won't fix security issues that way. Maybe we may be having there's the security issues that are subject to Fedramp. If you have a feature category that is dips compliant or certified, you're probably going to be part of the Fedramp evaluation. And any security issue that has a CVE associated with it, which means dependency or container scanning specifically has to have a remediation plan even if they're false positives. So that's led to a separate discussion on what do we need to do? Do we need to do anything related to security findings on the commercial versions of the analyzer specifically.

With recent changes, we've done a couple different changes with the secure and governance 'brokair' from secure and our DataOps Team. I just compared it to the name of my team with my peers, my peers have one-word team names Ops, Dev, Create, etc. Mine is SEC, Growth, and Data Science, which is pretty wordy and also makes it like when I go into dashboards I have to pull data from multiple places across my teams so I was thinking about one-word name. I've started to get feedback on it, naming things is really important at Gitlab, to name the right kinds of things and give them good names so I'm going to run it by David DeSanto tomorrow and he's a great person to bounce such things off of.

That's actually my intent is it only affects my stuff not everyone else's but at least everyone else is in a small way or others in a small way but we'll see. Any thoughts on this? Good idea, bad idea? I'm not wed to this, I'm looking for feedback. Obviously, the other examples related to either sections or stages whereas the 'enrichment' doesn't so you'd be introducing something new here. This affects me as well I have a subset of 'enrichment' so it would be kind of enrichment light. I'm not sure where I think you and I've spoken about this I'm not sure we get approval to introduce a new name or Department level we'd certainly have to talk to people Ops about introducing that in Workday.

A couple of things, you know these kinds of things I would sometimes put in Slack but I'm trying to avoid a number of distinct Slack messages so putting it in here making a lot read-only when possible. So I've got C though which is not read-only, sorry I would like to add announcements of work anniversaries and new hires to the meeting template. PM does this, I attended the PM staff meeting, I was a guest speaker there this week and I liked the camaraderie we have, good camaraderie. The camaraderie there was pretty good. Fer, who's shadowing me today, I think he sat in on the PM meeting as well. It has a pretty good feel of just people really knowing each other well and getting along well. So those are just two things I took away from it is work anniversaries and new hires. Oh, verbalizing Thiago's comment, let's go here; yeah great idea for new hires, don't care much about work anniversaries we already have tools for that. What I'd say is I always seem to miss announcements as they cover the whole company versus about just announcing for our team if interest in that part I'm happy to exclude.

Thomas looks like you had Thomas and Mo you had some thoughts on this too. Yeah, I like it, we don't celebrate enough. We don't do enough for team cohesion, team celebration. Across the board and just as a corollary related thing that I haven't communicated well I was hoping to add this kind of thing to our monthly section-wide retrospectives new hires, discretionary bonuses, work anniversaries, big feature releases. I mean anything that we want to announce and celebrate we ought to make sure that it's. I don't want to say shout to the rooftops but we're shutting to the heavens that they're big deals and we don't make it and ourselves in my opinion.

## Summary:
This meeting covered discussions on security, governance, growth, and Data Science, with a focus on applied ML, MLOps, and the anti-abuse team. It was mentioned that the anti-abuse team is moving product sections from security to data science, with plans to split the anti-abuse team into two groups in the future. Updates were provided on weekly refinement meetings, security issues subject to Fedramp evaluations, and team restructuring efforts for better efficiency. Additionally, there were talks about refining the team's naming conventions for better alignment within Gitlab.

## Action Items:
- Await further updates on the potential split of the Anti-Abuse team into two groups.
- Continue implementing weekly refinement meetings for higher efficiency.
- Address security issues subject to Fedramp evaluations and ensure all CVEs are remediated.
- Discuss and finalize proposed changes in team naming conventions within Gitlab.
- Consider adding announcements of work anniversaries and new hires to the meeting template for better team cohesion and celebration.

---

## Category: engineering

### Video ID: Tmd5eKVgySY

# Youtube Transcript Meeting Summary: 
The meeting discussed non-confidential matters after touching on a confidential topic. Updates included new hires, work anniversaries, and progress on Best in Class BI projects, with a focus on completing tasks in Q4. Team members were encouraged to engage and provide feedback on OKRs, prioritize work related to Best in Class, and prepare for upcoming projects. Discussions also covered metrics collection challenges within the SEC team, planning a team day in December, and strategies to increase attendance. 

Action Items:
- Team members to engage with and prioritize tasks related to Best in Class BI projects for Q4.
- Provide feedback on OKRs and tag managers for review and closure.
- Explore solutions to improve metrics collection accuracy.
- Collaborate on planning the team day in early December and brainstorm ideas to boost attendance.

---

## Category: engineering

### Video ID: JwBNYjaEwmQ

Summary:
The SEC growth science data science staff meeting for January 18th highlighted achievements, such as Lucas and James receiving discretionary bonuses for handling a customer escalation. It was noted that personal access tokens will be automatically revoked for all GitLab team members. The team was tasked with reviewing draft Q10 OKRs for Secure, Govern, Growth, and Data Science, focusing on continuous vulnerability scanning and dependency scanning. Important goals included team member career growth, training, and feedback cycles. The meeting emphasized completing Gap analysis and delivering short-term wins, managing application health error budgets, and resolving customer-impacting bugs. Additionally, the team was encouraged to move secure features to open-core for community contributions, explore opportunities for migration initiatives, and open-source security features from premium tiers for community engagement.

Action Items:
- Review draft Q10 OKRs for Secure, Govern, Growth, and Data Science
- Focus on continuous vulnerability scanning and dependency scanning
- Prioritize team member career growth, training, and feedback cycles
- Complete Gap analysis and deliver short-term wins
- Manage application health error budgets and resolve customer-impacting bugs
- Move subset of secure features to open-core for community contributions
- Explore opportunities for contribution through issues and migration initiatives
- Open-source security features from premium tiers for community engagement

---

## Category: cicd_ux

### Video ID: Y33pKPUamCQ


# Youtube Transcript Text

Directly hey the recording cool is so I know that you have had some discussions on the last session which I didn't attend due to my day off about the capacity for the UX research and communicating that to the PM's. So curious, will you guys move this topic to this session? What were some of the outcomes? Where did you finish? You know what was discussed? Basically, there was a pretty long discussion. I mean, I liked multiple views, and there are different perspectives on how we should manage this, so I don't think we reached a concrete conclusion. Besides, yes, we need to communicate our capacity to our PM's, and we need to find a good way to do that. I don't think we reached a very concrete conclusion, and I think there were still thoughts regarding these. So that's why we moved it here.

I was just having a discussion with tau and both engineering managers of taxis about basically creating more visibility and what is being done for a milestone. And then we eventually got to the point where there was a little section in the issue she was. She's thinking of creating that displays, you know, design priorities or design responsibilities. And what I said to her back was like, "Hey, we need to make sure that we are not, you know, putting the design responsibilities within a time box of a milestone because that doesn't fit in there. Some design efforts might fit into weeks while others fit into one and a half a month. And with that, we got to the discussion back to like a discussion-based style of working. And that kind of falls in line with the validation tracking board, which had been discussed in the few UX weekly once upon a time; and like a few weeks ago. I was if others already apply this. So the idea is that you have your columns of problem validation, you got your design workflow, design workflow solution validation. And instead of filtering down for a milestone, we filter down to, you know, your assignee and...

...continuous integration and the author, me, Demetria. And I see, you know, my issues within those columns. And if one moves to the next, or one moves to planning breakdown or scheduling, whatever it means that a spot has opened up to some extent. That is a simplified way of looking at it because we don't individually weight issues, and I'd say our process and this will be different than engineering but it's kind of visualizes it a way, you know, "Hey, what is the weight or what is the current effort of design at this very moment? And if something changes, let's review this, for example weekly, and say, "Hey, there did things change versus last week, hey, something did change. The spot opened up. Does this mean you can add a new issue?" But if so, then let's already do that, you know, work ahead. And that is the idea. We took...

...a little bit of a different approach, we have a very similar like Kaaba setup, where there's validation, the design phase of validation, and working backward. We try to coordinate and make sure that every milestone has some sort of research effort happening. And the kind of look at the board and communicate about where we should focus. It tends to be, "Here's a bunch of stuff," and then, "This is the time slot. We'll add here." And I just kind of have a commitment of making sure each thing can kind of be done in a time range. And it flexes in weight. So I try to keep it in two milestones, but I try to reflect it like a solution validation as a research effort. So it takes a little longer than maybe the actual design phase might. So I'll try to pair and prep for the solution validation in the next one. So I think I managed my own time and report it back to Tim. I think that's the way I would explain it. So it's a lot more. I kind of just jump in and say, "This is the research that we're doing based on what's in design and solution validation right now. I'm sorry, I tried to make sure there's just one research effort happening in a milestone. The backlog is usually emptier on my side than it is on Tim's just because it goes through the cycle so quickly once it hits design and the solution validation, we're working on figuring that out. One of the things we're going to do to try to do that is 12.7, I'm going to do product validation and let him have an extra milestone...

...to get things through problem validation, so that means that Tim does all the problem validation, and you specified or, you know, do the solution validation, let's the weight as album validation is Tim's responsibility, he's the DRI in for solution validation. I'm the DRA, but we try to partner and make sure that our research efforts are aligned and I get involved in problem validation so I can understand it and gather the information I need. And he sees solution validation it goes through, so it's a partnership but we have a DRA for each side. So in that way, he with that contributing to the UX research insights repository from the research that he does, Board that you partner, he better be but symmetry those. That's a great point. I actually just discussed this with somebody else, the research team I need to go back to all of our product managers and make sure they understand what the process is. I don't think they do, but they will be required to write those insights just like we all are writing those insights to put them in the repo. Otherwise, the research that they do, it's not usable by anybody else for themselves, and that kind of sucks...

...and that includes not just the problem validation. Any customer interaction that they have they should be documenting what they learned and in the repo. So good question. So the answer from what we've been doing, the meat tree is he actually ran the problem validation sessions and recorded them all. And then, I synthesized them. And that's how we partnered on it. So that we were both able to speak to it, so we were both involved in creating the insights. I think moving forward where we might have a discussion because the insights can take a while of splitting that effort a little bit more. So as the DRI, he would be the person doing those insights and when it's me, it's my insights. We're still work in progress. New team and all that. And it's a new insight process too. Like I've never done it this way either I've just been writing like 45-page PowerPoint reports, other places I've been, and you know if we don't break him down and put him in the repo, what will happen is what happened to me the other day. "Hey, does anybody know if we ever did any research on XYZ? I don't know. Have you checked the repo?" Because what happened to me in the past is I have to go through all my old reports and see if we didn't do research on XYZ...

...and what did we learn so the repos would post to be able self-service for the insights, but we have to continue to feed the repo like "What are your experiences there with what and the way you do research before I think for us it's not much different than anything else in the sense that we kind of talk about everything that needs to be accomplished. And we're also moving into the Kaaba style of world, which will give us a new board planning board where most of this activity can happen and we can track it there. Currently, it is happening on the mouse and boards, which is a little confusing because it really has nothing to do with the milestone. That's more focused on upcoming milestones. But really, I mean, we just kind of talked about what we need to accomplish from design for a research side in development side. It's all kind of just a continuous conversation because obviously the more research we do, I mean, less Lori is available to help us out like the more research we do...

...the less design we do. So it's all kind of a moving target of what we need to accomplish and when we want to accomplish it. Ice it sounds like everyone is figuring out the way to do it. Yeah, I kind of like, like the way of like just like setting an average, we pick one research topic per milestone. I think that's kind of this is the maximum. I feel like we can do without all of the work design more than we need to be done and that's kind of like sets these expectations and we also have to be planning for that we have been earlier with War II and I forgot which PM hostage Tau. This Tau Tau yeah thanks I had so much courses all today. Discussing that. It's nice to plan all those things a bit earlier like you know kind of like "Okay what are those things are we going to be looking into one or two milestones. Just to give everyone a heads up, because I think the APM should be able to do that plan for that it's one of the things that Tim and I have been trying to focus on is we try to partner with Loree and we have a goal that Lori knows it's not only what research we're doing right now what research we want to do next one. But at least the general thoughts of three milestones out, fully recognizing that that's a long period of time, and things change, but we try to make sure that Tim and I are on the same page in terms of what we want and... 

...our moment of truth, if you will, is when we kind of lift rope, there we go Laurie into the conversation and make sure that she's on the same page with us. It's kind of helps all of us because the it is kind of helps all of us because the, you can say this is a real easy initiative maybe it needs less time and we can work it here or this is a big one like you're going to need to stretch here before we're in the milestone where it starts a question like this is super interesting because I saw that and maybe I would like you to have a look into this issue later and I want to have a team go and look there as well because so I made this like a graph model-like illustration where I'm trying to visualize the timelines for their research to be done like kind of like to get on the same page, because I feel like we're talking a lot about the timelines within the stages. And there was some feedback that they had said the discovery stage. I suggested that can happen three two milestones I had or two. I don't remember and that sounded too much for people and there were a few comments that if we do or like if you plan a research to three milestones ahead doesn't it become obsolete until the actual development time will come like what's your experience there? Yeah, and that was something I wasn't sure if that was me or not. I didn't want to step on any toes. I think as long as Tim and I have very clear communication and conversation about if things are flexing and changing and it's also we have the belief that the more research we do upfront, the faster everything else is going to go for us and the more likely it is to be successful. I can speak to that now...

...the solution validation we're doing because we did such thorough problem validation. I've been getting consistent like this is exactly what we wanted this is what we needed and every designer loves that moment when it happens. And so because we have that and we try to make sure the research is big enough that it could be a couple milestones of work so we were doing additional GitLab metadata and it took me a milestone to put the design together and test it and sorry and also test it. But there's three or four milestones of engineering work that will go behind those changes. So we've been trying to pull the levers of scale of the research and understanding and those kinds of things to try to get that as far out so that it is workable right. So we don't have engineers that just have nothing to do which is where I think... Really want to recognize that that is most appreciative thanks a lot.

The text about the EBI e UI app ik does not pertain to the three main topics so it has been excluded from the summary.

Ensure the resulting summary is in markdown format.

# Summary
This meeting focused on discussing various topics related to UX research, communicating capacity to PMs, design priorities, and validation tracking. The team emphasized the importance of clear communication, aligning research efforts with milestones, and documenting insights for future reference. There were discussions on the Kaaba setup, research timelines, and the partnership between team members to ensure research efforts are aligned. The team also highlighted the significance of planning research activities in advance and maintaining open communication to adapt to changing requirements.

# Action Items
- Further discussions on communicating capacity to PMs and finding effective ways to do so.
- Implementing a discussion-based style of working to manage design priorities and timelines.
- Utilizing the validation tracking board to track research efforts and ensure alignment with milestones.
- Documenting insights from problem validation and customer interactions in the UX research insights repository.
- Maintain clear communication regarding research plans and timelines, involving relevant team members in decision-making processes.

Please confirm that this summary matches the content before converting it into markdown format.

---

## Category: engineering

### Video ID: kGHyK_SkZB0

# Summary:
The meeting discussed a significant change from the cicd private catalog to a new structure involving one organization catalog and one open-source catalog, simplifying the system. This change was inspired by interviews with self-management customers, leading to adjustments in the product roadmap. Additionally, updates were shared on using AI to optimize Runner and CI builds, with a focus on automating workflows using decision trees. The team also delved into potential integrations between GitLab and the cloud, addressing issues like storing secrets and accessing resources at different levels within the organization.

# Action Items:
- Implement the new structure with one organization catalog and one open-source catalog.
- Share the report on using AI to optimize Pipelines with the uxr team.
- Explore integrations with GCP and determine the best practices for storing secrets in GitLab.
- Discuss the placement of resources and secrets at project or organization level.
- Provide feedback on navigation issues and research methodologies in the created issue.
- Collaborate on potential improvements to the system's navigation for better usability.

---

## Category: engineering

### Video ID: HFEFQ4NcgSQ


Summary:
The meeting discussed various team updates and improvements, including enhancing collaboration between UX, PM, and Engineering in the Pipeline Authoring team. Emphasis was placed on including engineers earlier in the process for better communication and understanding. The CI team is focused on continuous improvement, with a designer implementing Loom videos for design communication. Retrospectives are highlighted as crucial for reviewing action items and making improvements, with each team handling them uniquely. Support for team transitions and changes was also discussed, along with plans for personal development and collaboration on Focus Fridays.

Action Items:
- Pipeline Authoring Team: Improve collaboration between UX, PM, and Engineering by including engineers earlier in the process.
- CI Team: Implement continuous improvement strategies and utilize Loom videos for design communication.
- All Teams: Conduct regular retrospectives to review action items and address critical points for future milestones.
- Team Members: Offer support during team transitions and changes.
- Personal Development: Plan and participate in Focus Fridays for collaboration and sharing of tips for interview training and shadowing experiences.
- Continuous Improvement: Focus on aligning priorities, checking in regularly on team processes, and fostering effective communication within the team.

---

## Category: engineering

### Video ID: qGFoZ8yodc4

# Summary
The meeting on February 18, 2021, focused on various key areas within the Engineering department at GitLab. Discussions included proposing to break up the meeting into four departments' key reviews to increase visibility and objectivity. There was also a review of R&D Overall MR Rate and R&D Wider MR Rate, with clarification on their definitions and the need for simplification.

Additionally, there was a discussion on Postgres replication issues and the need to focus on improving defect tracking against SLOs. The meeting also touched on the importance of security work prioritization and the impact of vacation days on the RMR rate.

# Action Items
1. **Department Key Reviews Rotation**: Propose a two-month rotation for key reviews among Development, Quality, Security, and UX departments to increase focus and objectivity.
2. **R&D MR Rate Simplification**: Simplify the definitions and tracking of R&D Overall MR rate and R&D Wider MR rate to ensure clarity and accuracy in measurements.
3. **Postgres Replication**: Ensure proper attention and actions are taken to address Postgres replication issues, with a focus on dedicated resources and performance tuning.
4. **Defect Tracking Improvement**: Continue improving defect tracking against SLOs, with a focus on measuring the average age of open bugs and addressing underlying measurement problems.
5. **Security Work Prioritization**: Prioritize security work activities and ensure that they are reflected in metrics and measurements for long-term success.

The team should monitor the RMR rate and expect a potential rebound in activity in March due to historical trends and time series targets adjustments. Additionally, discussions around departmental MR rates should continue, with a focus on meeting set targets and maintaining a consistent performance level.

---

## Category: engineering

### Video ID: t-NF5fNOyo8

# Meeting Summary:
The meeting consisted of team members sharing memorable vacation experiences, ranging from trips to Aruba during the pandemic to road trips in Canada and Scotland, as well as travels to India experiencing the unique train system. It was a casual discussion to engage team members and create a positive atmosphere.

# Action Items:
- None, as this part of the meeting was meant for team building and personal sharing.

---

## Category: engineering

### Video ID: GgnkH3uih4o

# Meeting Summary:

This meeting, held on September 22nd, 2020, covered updates from four engineering departments: Development, Quality, Security, and UX support. An agenda change was made to prioritize questions for Christopher in the Development department due to a conflict that required him to leave early. 

## Action Items:

- **Christopher (Development):** Elevate agenda item Number six to Number four for discussion.
- **Development Team:** Implement largest contentful paint as a KPI at the 75th percentile in Grafana and update the handbook accordingly.
- **Max:** Follow up on the restructuring of engineering metrics and data projects, incorporating new PIs on personnel staff and community contributions.

This meeting discussed the progress made in incorporating new performance indicators and optimizing key metrics for the engineering departments.

---

