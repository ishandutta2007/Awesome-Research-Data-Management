# Awesome-Research-Data-Management

## Top Research Data Management Ecosystem

**Curated List of SaaS Products & Open-Source GitHub Projects**  
*Focused on Research Data Repositories, FAIR Data, Data Management Plans, Institutional RDM, Metadata & Open Science Infrastructure*  

**Last updated: September 2026**

This repository tracks notable **SaaS/hosted platforms** and **open-source projects** for **Research Data Management (RDM)**. These systems help researchers and institutions store, describe, preserve, share, and cite research data while supporting Data Management Plans (DMPs), FAIR principles, and open-science workflows.

**Examples** include LabKey, Figshare, Dryad, Dataverse, Open Science Framework (OSF), Symplectic Elements, Pure, Converis, Zenodo, and DMPTool (the category leaders).

**Open-source emphasis**: Research Data Management has one of the strongest open-source ecosystems of any domain. **Dataverse**, **InvenioRDM** (the software behind Zenodo), **Open Science Framework**, **CKAN**, **DSpace**, and related projects power many institutional and national repositories. This section is heavily expanded with every major active project.

Contributions welcome! Open a PR to add/update entries. Keep descriptions factual and link to official sites.

## Table of Contents

- [SaaS/Hosted Platforms](#saas-hosted-platforms)
- [Open-Source GitHub Projects](#open-source-github-projects)
- [How to Contribute](#how-to-contribute)
- [Disclaimer](#disclaimer)

## SaaS/Hosted Platforms

**Market Context**: The Research Data Management and repository sector is estimated at **$2–3 billion annually** (2025–2026), encompassing institutional CRIS platforms, generalist data repositories, DMP tools, and enterprise research information systems. The sector is **moderately fragmented** — a few large incumbents (Elsevier/RELX, Springer Nature, Digital Science) dominate the CRIS/institutional segment, while the generalist repository space has many players (Figshare, Dryad, Zenodo, OSF) with no single winner-take-all dynamic. Open-source projects like Dataverse, DSpace, and CKAN ensure no vendor can fully lock in the market. The sector is expected to grow at ~8–12% CAGR driven by mandates for FAIR data and open science from funders like NIH, NSF, and the European Commission.

| Product | Parent Company | Revenue / Market Cap | Starting Price | Free Tier / Trial Limit |
|---------|---------------|---------------------|----------------|------------------------|
| [**Pure**](https://www.elsevier.com/products/pure) | [Elsevier (RELX)](https://www.relx.com/) | **Revenue ~$3.9B/yr** (Elsevier); RELX market cap **~$60B** | Custom (enterprise institutional license, typically $50K–$200K+/yr) | No free tier; no public trial — demo available on request |
| [**Figshare**](https://figshare.com/) | [Digital Science (Holtzbrinck)](https://www.digital-science.com/) | **Revenue ~$165M** (Digital Science); parent Holtzbrinck **~$1.2B rev** | **$875** one-time for 250 GB (Figshare+); institutional plans available | **20 GB** storage free forever; max 20 GB per individual file |
| [**Symplectic Elements**](https://www.symplectic.co.uk/) | [Digital Science (Holtzbrinck)](https://www.digital-science.com/) | **Revenue ~$165M** (Digital Science); parent Holtzbrinck **~$1.2B rev** | Custom (enterprise institutional license, typically $30K–$150K+/yr) | No free tier — institutional license only |
| [**LabKey**](https://www.labkey.com/) | LabKey Software (private) | **~$7M revenue**; ~36 employees | **$6,540/yr** (LIMS Starter, 5 users) to **$59,400/yr** (LIMS Enterprise, 10 users) | No free tier; **free trial available** on request |
| [**Dryad**](https://datadryad.org/) | Dryad (501(c)(3) nonprofit) | **~$3–5M/yr revenue** (nonprofit) | **$150** per dataset (≤5 GB), scaling to $808 (≤100 GB), $1,528 (≤250 GB) | No free tier — fee waiver available for low-income countries (World Bank classification); institutional partners may pre-pay DPCs |
| [**Zenodo**](https://zenodo.org/) | CERN (intergovernmental org) | Funded by CERN & EU OpenAIRE (~**€1.2B** CERN annual budget share) | **Free** for researchers (no paid tier) | **Free forever** — 50 GB per record, up to 100 files per record; no cap on total deposits; larger quotas on request |
| [**Open Science Framework (OSF)**](https://osf.io/) | [Center for Open Science](https://www.cos.io/) (501(c)(3) nonprofit) | **$10.2M revenue** (FY2024, mostly grants) | **Free** for researchers (no paid tier) | **Free forever** — 5 GB per private project, 50 GB per public project; unlimited components per project |
| [**DMPTool**](https://dmptool.org/) | [California Digital Library](https://cdlib.org/) (UC system) | Part of UC/CDL budget (**~$400M+** CDL annual) | **Free** for all users (no paid tier) | **Free forever** — unlimited DMPs, no storage limits (planning tool, not a data repository) |

## Open-Source GitHub Projects

The open-source RDM ecosystem is extensive. The table below lists all major active projects with their primary use case, GitHub stars, and license.

| Project | Description | Primary Use Case | GitHub | License |
|---------|-------------|-----------------|--------|---------|
| [**Dataverse**](https://github.com/IQSS/dataverse) | Leading open-source research data repository software developed at Harvard's IQSS. Supports sharing, citing, preserving, and discovering research data with a flexible, multi-level "Dataverse" collection model. Widely deployed by universities and consortia. | Institutional data repository | [IQSS/dataverse](https://github.com/IQSS/dataverse) (⭐ 900+) | Apache-2.0 |
| [**InvenioRDM**](https://inveniosoftware.org/products/rdm/) | Turn-key open-source research data management repository platform built on the Invenio Framework. Zenodo is the flagship public instance; institutions can run their own InvenioRDM repositories. | Generalist / institutional repository | [inveniosoftware/invenio](https://github.com/inveniosoftware) (⭐ 700+) | MIT |
| [**Open Science Framework (OSF)**](https://github.com/CenterForOpenScience/osf.io) | Open-source platform for the entire research lifecycle — project management, collaboration, versioning, pre-registration, and data sharing — developed by the Center for Open Science. | Research lifecycle & preregistration | [CenterForOpenScience/osf.io](https://github.com/CenterForOpenScience/osf.io) (⭐ 1.5k+) | MIT |
| [**CKAN**](https://github.com/ckan/ckan) | Widely used open-source data portal and catalog software, frequently adopted for research data catalogues, governmental open data, and institutional data discovery. | Data catalog / portal | [ckan/ckan](https://github.com/ckan/ckan) (⭐ 4.3k+) | AGPL-3.0 |
| [**DSpace**](https://github.com/DSpace/DSpace) | Long-established open-source repository software used by libraries and institutions for publications, theses, and increasingly for research data. | Institutional repository | [DSpace/DSpace](https://github.com/DSpace/DSpace) (⭐ 1.2k+) | Apache-2.0 |
| [**Samvera / Hyrax**](https://samvera.org/) | Community-developed repository framework (Ruby on Rails + Fedora) powering institutional data repositories like Deep Blue Data (U Michigan) and Imago (Indiana). | Institutional repository | [samvera/hyrax](https://github.com/samvera/hyrax) (⭐ 200+) | Apache-2.0 |
| [**Archivematica**](https://www.archivematica.org/) | Open-source digital preservation system implementing ISO 16363 (Trusted Digital Repository). Manages ingest, processing, and storage of AIPs/DIPs for long-term access. | Digital preservation | [artefactual/archivematica](https://github.com/artefactual/archivematica) (⭐ 350+) | AGPL-3.0 |
| [**OpenRefine**](https://github.com/openrefine/openrefine) | Java-based power tool for cleaning, transforming, and reconciling messy tabular data. Widely used for metadata cleanup, name reconciliation, and data preparation in RDM workflows. | Data cleaning & reconciliation | [openrefine/openrefine](https://github.com/openrefine/openrefine) (⭐ 10k+) | BSD-3-Clause |
| [**iRODS**](https://irods.org/) | Integrated Rule-Oriented Data System — policy-based data management middleware for large-scale, distributed storage environments. Used by national labs and research computing centers. | Policy-based distributed data mgmt | [irods/irods](https://github.com/irods/irods) (⭐ 100+) | BSD-3-Clause |
| [**CEDAR Metadata Tool**](https://github.com/metadatacenter) | Metadata schema authoring and template management platform developed by Stanford. Generates high-quality metadata conforming to community standards for FAIR data. | Metadata authoring | [metadatacenter/cedar](https://github.com/metadatacenter) (⭐ 60+) | BSD-2-Clause |
| [**Renku**](https://renku.io/) | Collaborative platform for reproducible and reusable data science. Built on knowledge graphs, Git, and containers to link code, data, and narrative for research workflows. | Reproducible research workflows | [RenkuML/renku](https://github.com/SwissDataScienceCenter/renku) (⭐ 250+) | Apache-2.0 |
| [**DVC (Data Version Control)**](https://dvc.org/) | Open-source version control system for ML/data science projects. Manages large files, datasets, and ML models using Git-like semantics with cloud storage backends. | Data & ML model versioning | [iterative/dvc](https://github.com/iterative/dvc) (⭐ 14k+) | Apache-2.0 |
| [**Fedora Repository**](https://fedorarepository.org/) | Flexible, extensible, open-source digital repository platform often paired with Samvera/Hyrax for institutional repository infrastructure. Supports linked data and scholarly objects. | Digital repository infrastructure | [fcrepo/fcrepo](https://github.com/fcrepo/fcrepo) (⭐ 150+) | MIT |

### Related Open Metadata & Standards Tooling

- **Metadata & standards**: [CEDAR](https://github.com/metadatacenter), [schema.org](https://schema.org/), [DataCite](https://datacite.org/), [Dublin Core](https://www.dublincore.org/), and related open metadata tooling.
- **FAIR assessment**: Community tools that evaluate datasets against FAIR principles.
- **Lab / ELN integration**: Open electronic lab notebooks and connectors that feed data into repositories.
- **Preservation systems**: [Archivematica](https://www.archivematica.org/) and similar open digital-preservation pipelines often paired with repositories.
- **Search & discovery**: Elasticsearch/OpenSearch-based discovery layers used by Invenio, Dataverse, and CKAN.
- National and institutional deployments of Dataverse, InvenioRDM, or CKAN as the core of a research data service.

---

**Frameworks for building custom systems**:  
The strongest open-source foundations are **Dataverse** (especially for institutional data repositories) and **InvenioRDM** (for Zenodo-style generalist or institutional repositories).  
**OSF** provides an open platform for project-centric research workflows.  
**CKAN** and **DSpace** remain excellent for catalogs and hybrid publication/data repositories.  
**Samvera/Hyrax + Fedora** is a powerful stack for institutions wanting a Ruby-based, highly customizable repository.  
These can be combined with open metadata tools, preservation systems, and authentication infrastructure.  

Hosted services (Figshare, Dryad, Zenodo.org, OSF.io, LabKey Cloud, commercial CRIS platforms) offer convenience, curation, and support. Many institutions run self-hosted Dataverse or InvenioRDM instances while also recommending Zenodo or domain repositories to their researchers.

## How to Contribute

1. Fork the repo.
2. Add/edit entries in `README.md` (follow existing format).
3. Include: name, link, 1–2 sentence description, and whether it's SaaS/hosted or open-source.
4. Submit PR with a short explanation.

Star the repo if you find it useful!

## Disclaimer

- This is a **community-curated** list — not exhaustive and not an endorsement.
- Research data often includes sensitive, personal, or proprietary information. Access controls, consent, licensing, and long-term preservation planning are essential.
- Open-source RDM platforms provide transparency, community governance, and freedom from vendor lock-in, but still require institutional commitment to hosting, curation, and sustainability. Evaluate governance, funding, and support models carefully.

---

**Made for research data stewards, librarians, research software engineers, open-science advocates, and institutional research offices.**  
Let's strengthen the global open infrastructure for research data so that knowledge remains findable, accessible, interoperable, and reusable.
