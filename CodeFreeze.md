# CodeFreeze Pipeline Integration

## Summary
Block the merging on PRs when a code freeze is in progress by checking a dedicated LaunchDarkly feature flag.

---

## Freezing a TIER 🥶

Triggering a code freeze is done by turning on the `code-freeze` feature flag found in the `smart-assistant` project. 

### Toggling LaunchDarkly Feature Flags in Slack
In the `phsdig.slack.com` workspace, the LaunchDarkly (LD) App had already been setup for us to toggle a specific LD flag to freeze a specific TIER.

<details>
<summary><b>Show Instructions</b></summary>

**You can update a flag by running the following Slack command:**
> `/ld flag smart-assistant <dev or stage> code-freeze`

**You'll see the following message populated, select the '...':**
![ld_details](./resources/LD_Flag_Details.png)

**You can now toggle the flag on/off with the following option:**
![ld_toggle](./resources//LD_Flag_Toggle.png)

</details>

</br>

---

## What a code freeze looks like 👀

<details>
<summary><b>Show Details</b></summary>

When there is a code freeze in a particular tier, this fail the `Check Code Freeze` workflow with an exception such as this:
![gh_codefreeze_exception](./resources/GH_CodeFreeze_Exception.png)

</details>
</br>

---

## How it works 🤔
<details>
<summary><b>Show Details</b></summary>

### Tech Stack
- GitHub Actions
- LaunchDarkly

### Setup in new Github Repositories
- Add the LaunchDarkly API key as `LD_API_KEY` (found in the SmartAssistant 1Password vault) in **Settings > Secrets > Actions**
- Add the `CodeFreeze.yml` workflow file and the `code_freeze.py` Python script to the `.github/workflows` directory.

</details>
</br>

---

## FAQ 🙋
<details>
<summary><b>Show Details</b></summary>

- **What if the code freeze is over and I want to merge my blocked PR?**
  - If the job failed due to the code freeze as seen in [What a code freeze looks like](#what-a-code-freeze-looks-like), navigate to the failed GH action run and rerun the failed job. If the code freeze is over, this should succeed.
- **Why is my PR blocked when we're not in a code freeze?**
    - The workflow is failing due to setup or an issue with the Python script. Checkout the logs and bring this up to the team if you need help troubleshooting.
    - The `code-freeze` LaunchDarkly flags were not toggled off to reflect the team's claim of a code freeze being over. There is currently no automation to the toggle of these flags, it is manual, even through Slack.
</details>
