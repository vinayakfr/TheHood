# pages/rule_book.py

import reflex as rx
from typing import List, Dict, Literal, Optional, Tuple
from dataclasses import dataclass

# ---- Domain Models ----

RoleName = Literal["OG", "Shot Caller", "Soldier", "Youngin/Shorty"]

@dataclass
class RoleConfig:
    name: RoleName
    title: str
    description: str
    max_count: int
    can_invite: bool
    can_promote: bool
    can_demote: bool
    moderation_power: Literal["none", "limited", "full"]
    voting_power: Literal["none", "standard", "high"]
    escalation_contact: Optional[RoleName] = None

@dataclass
class Responsibility:
    role: RoleName
    items: List[str]

@dataclass
class PromotionRule:
    from_role: RoleName
    to_role: RoleName
    prerequisites: List[str]
    min_days_in_role: int
    required_approvals: List[RoleName]
    forbidden_conditions: List[str]

@dataclass
class MembershipPolicy:
    invites_enabled: bool
    invite_who_can_send: List[RoleName]
    invite_prerequisites: List[str]
    signup_requirements: List[str]
    login_factors: List[str]
    probation_days: int
    probation_rules: List[str]
    removal_rules: List[str]
    rejoin_rules: List[str]

@dataclass
class CommunicationRule:
    title: str
    details: List[str]

@dataclass
class TagDefinition:
    tag: str
    meaning: str
    usage_examples: List[str]
    who_can_use: List[RoleName]

@dataclass
class TurfDefinition:
    name: str
    description: str
    moderators: List[RoleName]
    posting_rules: List[str]


# ---- Configuration Data ----

ROLE_CONFIGS: Dict[RoleName, RoleConfig] = {
    "OG": RoleConfig(
        name="OG",
        title="Respected Elder",
        description="Council of respected elders; guardians of culture, ethics, and long-term direction.",
        max_count=3,
        can_invite=True,
        can_promote=True,
        can_demote=True,
        moderation_power="full",
        voting_power="high",
        escalation_contact=None,
    ),
    "Shot Caller": RoleConfig(
        name="Shot Caller",
        title="Decision Maker",
        description="Operational leaders; make calls on missions, resolve conflicts, and coordinate squads.",
        max_count=7,
        can_invite=True,
        can_promote=True,
        can_demote=False,
        moderation_power="full",
        voting_power="high",
        escalation_contact="OG",
    ),
    "Soldier": RoleConfig(
        name="Soldier",
        title="Foot Soldier",
        description="Core contributors; execute tasks, maintain standards, and mentor Youngins.",
        max_count=50,
        can_invite=False,
        can_promote=False,
        can_demote=False,
        moderation_power="limited",
        voting_power="standard",
        escalation_contact="Shot Caller",
    ),
    "Youngin/Shorty": RoleConfig(
        name="Youngin/Shorty",
        title="New Joinee",
        description="New members under probation; learn norms, complete onboarding missions.",
        max_count=15,# practical upper bound
        can_invite=False,
        can_promote=False,
        can_demote=False,
        moderation_power="none",
        voting_power="none",
        escalation_contact="Soldier",
    ),
}

RESPONSIBILITIES: List[Responsibility] = [
    Responsibility(
        role="OG",
        items=[
            "Define ethics, cultural norms, and code of conduct.",
            "Act as final escalation for disputes and bans.",
            "Ratify strategic missions and long-term plans.",
            "Safeguard brand voice and external partnerships.",
        ],
    ),
    Responsibility(
        role="Shot Caller",
        items=[
            "Own mission planning and execution.",
            "Allocate squads and assign roles per mission.",
            "Resolve conflicts swiftly; escalate to OGs if needed.",
            "Host weekly debrief and maintain KPIs.",
        ],
    ),
    Responsibility(
        role="Soldier",
        items=[
            "Deliver assigned tasks to spec and on time.",
            "Maintain documentation, changelogs, and retros.",
            "Mentor Youngins; verify onboarding checklists.",
            "Flag risks early; propose improvements.",
        ],
    ),
    Responsibility(
        role="Youngin/Shorty",
        items=[
            "Complete onboarding module and probation missions.",
            "Learn tags, posting etiquette, and escalation paths.",
            "Attend weekly syncs; shadow Soldiers.",
            "Demonstrate reliability and constructive communication.",
        ],
    ),
]

PROMOTION_RULES: List[PromotionRule] = [
    PromotionRule(
        from_role="Youngin/Shorty",
        to_role="Soldier",
        prerequisites=[
            "Complete probation checklist and 3 minor missions.",
            "Zero violations in the last 30 days.",
            "Positive feedback from at least 2 Soldiers.",
        ],
        min_days_in_role=14,
        required_approvals=["Shot Caller"],
        forbidden_conditions=[
            "Open moderation flags unresolved.",
            "Negative behavior or toxicity reports in last 30 days.",
        ],
    ),
    PromotionRule(
        from_role="Soldier",
        to_role="Shot Caller",
        prerequisites=[
            "Lead 2 missions end-to-end with successful outcomes.",
            "Document SOPs for a recurring workflow.",
            "Demonstrate conflict resolution and mentorship impact.",
        ],
        min_days_in_role=45,
        required_approvals=["OG"],
        forbidden_conditions=[
            "Unresolved delivery breaches.",
            "Pattern of missed deadlines or poor documentation.",
        ],
    ),
    PromotionRule(
        from_role="Shot Caller",
        to_role="OG",
        prerequisites=[
            "Sustained stewardship for 90 days with high trust.",
            "Propose and ratify one strategic initiative.",
            "Exemplary ethics and community-first decisions.",
        ],
        min_days_in_role=90,
        required_approvals=["OG"],
        forbidden_conditions=[
            "Conflict of interest without disclosure.",
            "Repeated unilateral decisions against consensus.",
        ],
    ),
]

MEMBERSHIP_POLICY = MembershipPolicy(
    invites_enabled=True,
    invite_who_can_send=["OG", "Shot Caller"],
    invite_prerequisites=[
        "Prospect must have a portfolio or demonstrable work.",
        "References from at least one Soldier.",
        "Agreement to Code of Conduct and privacy notice.",
    ],
    signup_requirements=[
        "Valid email and passkey/2FA setup.",
        "Profile fields: display name, role intent, skills.",
        "Acceptance of Terms of Service and Community Guidelines.",
    ],
    login_factors=[
        "Password or passkey",
        "Time-based OTP (TOTP) or WebAuthn",
        "Device verification for new sessions",
    ],
    probation_days=14,
    probation_rules=[
        "Limited posting; must use prescribed tags.",
        "All posts require Soldier review.",
        "No DMs for solicitations; keep comms in threads.",
    ],
    removal_rules=[
        "3 major violations in 60 days → removal vote by Shot Callers.",
        "Harassment, hate speech, or doxxing → immediate ban by OGs.",
    ],
    rejoin_rules=[
        "Cooling-off period of 30 days.",
        "Post-mortem with Shot Caller and acceptance of remediation plan.",
    ],
)

COMMUNICATION_RULES: List[CommunicationRule] = [
    CommunicationRule(
        title="Tone & Respect",
        details=[
            "No personal attacks, harassment, bigotry, or slurs.",
            "Assume positive intent; critique ideas, not people.",
            "Use inclusive language; avoid gatekeeping.",
        ],
    ),
    CommunicationRule(
        title="Posting Etiquette",
        details=[
            "Write clear titles, concise bodies, and actionable asks.",
            "Use correct tags; one primary tag per post.",
            "Add context: goals, constraints, expected output, blockers.",
        ],
    ),
    CommunicationRule(
        title="DMs & Off-Thread",
        details=[
            "Keep decisions in public threads; summarize DMs in-channel.",
            "No unsolicited promotions or spam.",
            "Respect boundaries; no repeated pings.",
        ],
    ),
    CommunicationRule(
        title="Escalations",
        details=[
            "Report issues with the appropriate tag (to be shared).",
            "Escalate to Soldier → Shot Caller → OG chain when needed.",
            "Document facts; avoid speculation.",
        ],
    ),
]

TURFS: List[TurfDefinition] = [
    TurfDefinition(
        name="Build Lab",
        description="Project execution, sprints, reviews, and retros.",
        moderators=["Shot Caller", "OG"],
        posting_rules=[
            "All tasks must reference a mission and owner.",
            "Daily standups use the standup tag.",
            "Retros must include wins, misses, and next steps.",
        ],
    ),
    TurfDefinition(
        name="Culture Corner",
        description="Community updates, shoutouts, and celebrations.",
        moderators=["Soldier", "Shot Caller"],
        posting_rules=[
            "Use shoutout tag to recognize contributions.",
            "No callouts; keep feedback constructive.",
            "Images/videos must comply with content policy.",
        ],
    ),
]

# Placeholder: tag glossary will be injected when you share the list.
TAG_DEFS: List[TagDefinition] = [
    # Example structure for future injection:
    # TagDefinition(tag="mission", meaning="Work item or initiative", usage_examples=["mission: revamp auth"], who_can_use=["Soldier", "Shot Caller", "OG"])
]


# ---- Utility Logic ----

def get_role_relations() -> List[Tuple[RoleName, Optional[RoleName]]]:
    """Return (role, escalation_contact)."""
    return [(rc.name, rc.escalation_contact) for rc in ROLE_CONFIGS.values()]

def get_role_limits() -> Dict[RoleName, int]:
    return {rc.name: rc.max_count for rc in ROLE_CONFIGS.values()}


# ---- UI Components ----

def section(title: str, content: rx.Component) -> rx.Component:
    return rx.section(
        rx.heading(title, size="7", class_name="mb-3"),
        content,
        class_name="mb-10",
    )

def subsection(title: str, items: List[str]) -> rx.Component:
    return rx.box(
        rx.heading(title, size="5", class_name="mb-2"),
        rx.unordered_list(
            *[rx.list_item(rx.text(i, class_name="text-base")) for i in items],
            class_name="list-disc pl-6 space-y-1",
        ),
        class_name="mb-6",
    )

def rule_list(items: List[str]) -> rx.Component:
    return rx.unordered_list(
        *[rx.list_item(rx.text(i, class_name="text-base")) for i in items],
        class_name="list-disc pl-6 space-y-1",
    )

def role_card(cfg: RoleConfig, resp: Responsibility) -> rx.Component:
    return rx.box(
        rx.heading(f"{cfg.name} — {cfg.title}", size="5", class_name="mb-1"),
        rx.text(cfg.description, class_name="text-base mb-3"),
        rx.flex(
            rx.badge(f"Max: {cfg.max_count}", class_name="mr-2"),
            rx.badge(f"Moderation: {cfg.moderation_power}", class_name="mr-2"),
            rx.badge(f"Voting: {cfg.voting_power}"),
            class_name="mb-3 flex-wrap gap-2",
        ),
        rx.heading("Responsibilities", size="4", class_name="mb-2"),
        rule_list(resp.items),
        rx.divider(class_name="my-4"),
        rx.grid(
            rx.box(
                rx.heading("Powers", size="4", class_name="mb-2"),
                rule_list([
                    f"Can Invite: {'Yes' if cfg.can_invite else 'No'}",
                    f"Can Promote: {'Yes' if cfg.can_promote else 'No'}",
                    f"Can Demote: {'Yes' if cfg.can_demote else 'No'}",
                ]),
            ),
            rx.box(
                rx.heading("Escalation", size="4", class_name="mb-2"),
                rule_list([
                    f"Primary escalation: {cfg.escalation_contact or 'None'}",
                ]),
            ),
            columns="2",
            spacing="4",
            class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
        ),
        class_name="p-4 border rounded-lg bg-white/50",
    )

def promotion_card(rule: PromotionRule) -> rx.Component:
    return rx.box(
        rx.heading(f"{rule.from_role} → {rule.to_role}", size="5", class_name="mb-2"),
        rx.text(f"Minimum time in role: {rule.min_days_in_role} days", class_name="text-base mb-3"),
        rx.grid(
            rx.box(
                rx.heading("Prerequisites", size="4", class_name="mb-2"),
                rule_list(rule.prerequisites),
            ),
            rx.box(
                rx.heading("Required Approvals", size="4", class_name="mb-2"),
                rule_list([f"Approval from: {', '.join(rule.required_approvals)}"]),
            ),
            rx.box(
                rx.heading("Forbidden Conditions", size="4", class_name="mb-2"),
                rule_list(rule.forbidden_conditions),
            ),
            columns="3",
            spacing="4",
            class_name="grid grid-cols-1 md:grid-cols-3 gap-6",
        ),
        class_name="p-4 border rounded-lg bg-white/50",
    )

def turf_card(t: TurfDefinition) -> rx.Component:
    return rx.box(
        rx.heading(t.name, size="5", class_name="mb-1"),
        rx.text(t.description, class_name="text-base mb-3"),
        rx.flex(
            *[rx.badge(m) for m in t.moderators],
            class_name="mb-3 gap-2 flex-wrap",
        ),
        rx.heading("Posting Rules", size="4", class_name="mb-2"),
        rule_list(t.posting_rules),
        class_name="p-4 border rounded-lg bg-white/50",
    )

def tag_glossary(tags: List[TagDefinition]) -> rx.Component:
    if not tags:
        return rx.box(
            rx.text(
                "Tag glossary will be added once you share the tag list. This section supports per-tag meaning, usage examples, and role permissions.",
                class_name="text-base italic",
            ),
            class_name="p-4 border rounded-lg bg-yellow-50",
        )
    return rx.grid(
        *[
            rx.box(
                rx.heading(f"#{t.tag}", size="5", class_name="mb-1"),
                rx.text(t.meaning, class_name="text-base mb-2"),
                rx.heading("Usage Examples", size="4", class_name="mb-1"),
                rule_list(t.usage_examples),
                rx.heading("Who Can Use", size="4", class_name="mb-1 mt-2"),
                rx.flex(*[rx.badge(r) for r in t.who_can_use], class_name="gap-2 flex-wrap"),
                class_name="p-4 border rounded-lg bg-white/50",
            )
            for t in tags
        ],
        class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
    )


# ---- Page ----

def rule_book_page() -> rx.Component:
    role_limits = get_role_limits()
    relations = get_role_relations()

    # Map responsibilities by role
    resp_map: Dict[RoleName, Responsibility] = {r.role: r for r in RESPONSIBILITIES}

    return rx.container(
        rx.heading("Rule Book", size="9"),
        rx.separator(class_name="mt-6"),

        section(
            "About",
            rx.text(
                "This Rule Book defines roles, responsibilities, membership processes, promotion pathways, communication standards, tag usage, and turf-specific policies. It is the source of truth for how we operate.",
                class_name="text-lg mb-2",
            ),
        ),

        section(
            "Invites",
            rx.box(
                subsection("Who can invite", [f"{', '.join(MEMBERSHIP_POLICY.invite_who_can_send)}"]),
                subsection("Prerequisites", MEMBERSHIP_POLICY.invite_prerequisites),
                subsection("Probation", [
                    f"Probation duration: {MEMBERSHIP_POLICY.probation_days} days",
                    *MEMBERSHIP_POLICY.probation_rules,
                ]),
            ),
        ),

        section(
            "Log In",
            rx.box(
                subsection("Authentication Factors", MEMBERSHIP_POLICY.login_factors),
                subsection("Security Notes", [
                    "Do not share OTPs or recovery codes.",
                    "Enable passkeys/WebAuthn where possible.",
                    "Review active sessions periodically.",
                ]),
            ),
        ),

        section(
            "Sign Up",
            rx.box(
                subsection("Requirements", MEMBERSHIP_POLICY.signup_requirements),
                subsection("Privacy & Conduct", [
                    "Agree to Code of Conduct and content policy.",
                    "Consent to moderation in line with community guidelines.",
                ]),
            ),
        ),

        section(
            "Turfs",
            rx.grid(
                *[turf_card(t) for t in TURFS],
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
        ),

        section(
            "Mission",
            rx.box(
                rx.text(
                    "Missions are structured initiatives with defined owners, deliverables, and timelines.",
                    class_name="text-base mb-4",
                ),
                subsection("Shot Callers", [
                    "Define mission scope, success metrics, and timeline.",
                    "Assign squads and role responsibilities.",
                    "Run weekly syncs and publish debriefs.",
                ]),
                subsection("Soldiers", [
                    "Execute tasks, maintain documentation, and surface risks early.",
                    "Mentor Youngins on mission workflows.",
                ]),
                subsection("OGs", [
                    "Ratify strategic missions, arbitrate conflicts, and ensure ethical alignment.",
                ]),
            ),
        ),

        section(
            "Roles",
            rx.box(
                rx.grid(
                    *[role_card(ROLE_CONFIGS[r], resp_map[r]) for r in ROLE_CONFIGS.keys()],
                    class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6",
                ),
                rx.heading("Role Limits", size="5", class_name="mb-2"),
                rule_list([f"{role}: max {count}" for role, count in role_limits.items()]),
                rx.heading("Relations & Escalations", size="5", class_name="mt-4 mb-2"),
                rule_list([
                    f"{role} → escalate to {esc or 'N/A'}" for role, esc in relations
                ]),
            ),
        ),

        section(
            "Promotion Pathways",
            rx.grid(
                *[promotion_card(pr) for pr in PROMOTION_RULES],
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
        ),

        section(
            "Communication & Posting Rules",
            rx.box(
                *[subsection(cr.title, cr.details) for cr in COMMUNICATION_RULES],
                rx.box(
                    rx.heading("Content Policy", size="5", class_name="mb-2"),
                    rule_list([
                        "No hate speech, harassment, doxxing, or explicit content.",
                        "Credit sources; do not plagiarize.",
                        "Follow local laws and platform terms.",
                    ]),
                ),
            ),
        ),

        section(
            "Tag Glossary",
            tag_glossary(TAG_DEFS),
        ),

        section(
            "Leveling Up & Violations",
            rx.box(
                subsection("Leveling Principles", [
                    "Merit, consistency, and community impact are prioritized.",
                    "Documentation and mentorship weigh heavily.",
                    "Violations reset timers and may block promotion.",
                ]),
                subsection("Violations", [
                    "Minor: off-topic posts, incorrect tags, low-effort comments.",
                    "Major: harassment, spam, leaking private info.",
                    "Consequences escalate from warnings to bans per policy.",
                ]),
                subsection("Removal & Rejoin", [
                    *MEMBERSHIP_POLICY.removal_rules,
                    *MEMBERSHIP_POLICY.rejoin_rules,
                ]),
            ),
        ),

        class_name="max-w-5xl mx-auto py-10",
    )
