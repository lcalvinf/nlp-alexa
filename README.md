# Mini "Alexa" Project
## For NLP

If you're reading this, you probably already know what it's about. If you don't, you probably shouldn't be reading it, so go away.

I'll go over the details of how all this works in person, but a few general guidelines once you've gotten started:
- Commit messages should describe what the changes do at a **high level** and **why**, but not the implementation details.
  - If your commit does too much to easily describe it as a single high-level change, it should be more than one commit.
- If you make a change to the public API of your code (i.e. the part of your code that other people use), **say so in the commit message**.
  - Say **what** you changed, **why**, and **how** others will have to change the parts of their code to make it interact with yours properly.
  - If you're making changes too quickly for this to be reasonable (e.g. in early prototyping), write a comment above the unstable code saying
    it's unstable and others shouldn't depend on it. That way when someone's code breaks because they used it anyway, it's their own fault and
    not yours.
    - Don't use this as an excuse to not worry about public API changes. Only say something's unstable if you really are changing it constantly
      and you really don't know what the final API will look like.
- Your code should make use of comments to describe **how** and  **why** code is structured the way it is (if those things are unintuitive), and 
    any pertinent details for people using it (even if they are intuitive), but not to explain exactly **what** the code is doing. The code itself 
    should be clear enough to understand what it's doing without explanation; if you find yourself needing to explain it, you should probably 
    rethink its large-scale structure.
