# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

delegated: static HTML, CSS and vanilla JS with self-hosted fonts, no framework and no build step. A portfolio is a handful of documents; static files load instantly, deploy anywhere (Vercel, the tsveto.com domain), and will still build in ten years.

## Users

- Hiring managers, CTOs and founders evaluating Tsvetomir ("Tsveto") Batinov for a senior full-stack / applied-AI role or a contract. They arrive from a CV, LinkedIn or a cold message, usually on a laptop, and give the page one to three minutes.
- Technical reviewers (staff engineers) who want proof of depth: how systems are built, not just what they are called.
- Potential consulting clients of Delta Forge.

Assumption (not confirmed in an interview): the primary job is "decide whether to get on a call with Tsveto".

## Product Purpose

Show everything Tsveto has built, with enough architectural specificity that a senior reader believes it, and make contacting him effortless. Success: a reader leaves knowing three or four concrete systems he shipped end to end and clicks email or LinkedIn.

## Positioning

A founder-engineer who has shipped whole products alone: a 270k-line accounting platform with AI document extraction and VAT filing (TaxMate), two-sided Bulgarian marketplaces on a shared engine, and trading infrastructure for a quant fund, after five years leading a team at Risika. The combination of owning the product, the money path and the infrastructure, in a regulated domain, is the claim.

## Operating Context

Read on desktop between other tabs; sometimes opened on a phone from LinkedIn. Readers compare against other engineers' portfolios and GitHub profiles. Many of the repos are private, so the site is the only way to see the work.

## Capabilities and Constraints

- English. Product names that are Bulgarian keep their Cyrillic names (Намери фотограф, Намери Счетоводител, Намери чистач) with an English gloss.
- Hyperion is a client (quant hedge fund): describe architecture and responsibilities only. No code, no strategy details, no performance numbers.
- Toggl: plain contract developer role; mention, do not embellish.
- No fabricated metrics, testimonials, users or revenue. Numbers used must be measured from the repos (lines of code, modules, test files) or the CV.

## Brand Commitments

Name: Tsvetomir Batinov, goes by Tsveto. Domain tsveto.com. Title from CV: Senior Full-Stack & Applied AI Engineer. Based in Plovdiv, Bulgaria, remote (CET). Contact: tsbatinov@gmail.com, linkedin.com/in/tsvetomirbatinov, github.com/Sclipper. Tsveto asked for it to "look fucking awesome": ambitious, polished, multiple rounds and an adversarial review.

## Evidence on Hand

- CV: /mnt/project-files/cv/cv-source.html (roles, dates, stack).
- TaxMate (Sclipper/taxmate-api, taxmate-dashboard, taxmate-ocr, taxmate-mcp): NestJS + Prisma API with ~78 domain modules, 149 Prisma models, ~270k lines of TypeScript in src (excluding specs), 445+ spec files. Document AI + OpenAI fallback OCR, Qdrant classification, IRIS open banking (the CV says Salt Edge; the code uses IRIS), NAP VAT files (PRODAGBI/POKUPKI/DEKLAR in Windows-1251), payroll, Stripe plans, OAuth/OIDC MCP server.
- Намери фотограф + nameri-engine (DeltaForgeBG): photography marketplace on its own NestJS engine (the other two Намери sites are standalone apps) for requests, dispatch, offers, contact unlock, bookings, reviews; Stripe booking-fee pilot (Nov 2026).
- Намери Счетоводител (Sclipper/find-accountant): accountant RFP platform, Next.js 15, Claude brief enrichment, weighted proposal ranking.
- Намери чистач (DeltaForgeBG/find-cleaner): home-cleaning marketplace in Sofia, token-link auth, two-sided ratings.
- Fetchpaw (DeltaForgeBG/invoice-fetcher, fetchpaw.app): Chrome/Edge MV3 extension that collects supplier invoices in the user's signed-in browser; Jev picks each click, remembered invoice pages, asks before risky clicks, bank-statement gap check. ~10.6k lines TS in the extension, ~1.7k in the Node/Postgres/Stripe server; e2e against 5 fake portals. Plates are the site's own panel screenshots (fake data).
- opencal-sync (public, Sclipper/opencal-sync): self-hosted OneCal alternative, Google/Outlook mirroring via Composio, Docker + SQLite.
- Hyperion (HyperionQS org): research ingestion, LLM agents, LEAN engine, IB brokerage, gateways, order ledger, reconciler, data lake, Monte Carlo / factor research.
- Risika: CV facts only (team lead, React/D3, Node, AWS).
- No headshot, no screenshots, no testimonials on hand. Do not fabricate.

## Product Principles

1. Specific beats impressive: name the mechanism, the constraint and the trade-off.
2. The work leads; the person is introduced through what he built.
3. Respect client confidentiality visibly: say what is withheld and why.
4. One obvious way to get in touch, from anywhere on the page.

## Accessibility & Inclusion

WCAG 2.2 AA. Respect prefers-reduced-motion. Readable without JavaScript.
