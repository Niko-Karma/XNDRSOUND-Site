# SOP: SSH-in-Browser Access (Hybrid Automation)

**Purpose:** Protocol for establishing SSH access to the Google Cloud Production Environment using the Antigravity Browser Subagent, overcoming local CLI/SDK limitations.

## 1. Objective
To establish a reliable terminal interface with the GCP VM Instance without local `gcloud` tools.

## 2. Workflow Steps

### Phase 1: Navigation & Trigger
1.  **Agent Action:** Open Browser and navigate to **GCP Console > Compute Engine > VM Instances**.
2.  **Agent Action:** Locate the target instance (`web-server-main` or similar).
3.  **Agent Action:** Click the **"SSH"** button (or "Open in browser window" dropdown option).

### Phase 2: Authentication Gap (Human-in-the-Loop)
1.  **Agent Action:** **PAUSE** for 20-30 seconds.
2.  **Human Action:** The authenticated user must verify the connection popup (authorize the SSH key injection) or complete any OIDC login flow if prompted.
3.  **Constraint:** The Agent must *wait* and not attempt to interact until the terminal is visible.

### Phase 3: Execution & Persistence
1.  **Agent Action:** Detect the active terminal window (black screen with command prompt/text).
2.  **Agent Action:** Inject commands via keyboard events (e.g., `ls -la`, `cd /var/www/...`).
3.  **CRITICAL:** Do **NOT** close the browser window or navigate away. The window must remain open to maintain the active SSH connection.

## 3. Verified Success Evidence
*Test Date: 2025-12-08*
*Command:* `ls -la`
*Result:* Terminal successfully listed directory contents.

![SSH Terminal Evidence](C:/Users/alexc/.gemini/antigravity/brain/6f1baef3-be0b-449f-847e-94e5aa3119b9/uploaded_image_1765248649936.png)

## 4. Updates & Rollback
If this method fails:
1.  Notify the user immediately.
2.  Fallback: Ask user to perform manual SSH operations and paste output.
