### 🚀 DEPLOYMENT REQUEST
**From:** Technical Project Manager
**To:** DevOps / Release Engineer (Antigravity)
**Date:** 2025-12-09
**Target:** PRODUCTION (GCP)

---

### 1. RELEASE OVERVIEW
**Version:** 2.1 (Design & Feature Update)
**Summary:** Implementation of "Mailing List" CTA and "Clearcode" Partner Branding.

### 2. CHANGELOG (Artifacts to Deploy)
*   **Codebase:**
    *   `templates/index.html`: Added Top Navigation Link ("MAILING LIST"), Footer Button, & Clearcode Branding.
*   **Assets:**
    *   `static/img/clearcode_logo.jpg` (New File).

### 3. VERIFICATION STATUS
*   **QA Status:** **PASSED** ✅
*   **Critical Checks:**
    *   Mailing List Link (`symphony.to/...`): **VERIFIED**
    *   Footer Branding (Text + Logo): **VERIFIED**
    *   Layout/Responsiveness: **VERIFIED**
    *   Legacy Routes (`/staging`): **REMOVED**

### 4. DEPLOYMENT INSTRUCTIONS
1.  **Pull Changes:** `git pull origin main` (Ensure Fast-Forward).
2.  **Restart Service:** `sudo systemctl restart xndrsound` (Graceful reload).
3.  **Verify:** Check footer on `https://xndrsound.com`.

### 5. ROLLBACK STRATEGY
*   **Trigger:** If Footer breaks layout or Mailing Link 404s.
*   **Command:** `git reset --hard HEAD~1 && sudo systemctl restart xndrsound`

---
**End of Request**
