#!/usr/bin/env python3

""" AD1459, an IRC Client

  Copyright ©2019-2020 by Gaven Royer

  Permission to use, copy, modify, and/or distribute this software for any
  purpose with or without fee is hereby granted, provided that the above
  copyright notice and this permission notice appear in all copies.

  THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH REGARD
  TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
  FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
  DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
  ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
  SOFTWARE.

  This file is the licence for the project.
"""

__license__ = (
'    Mozilla Public License Version 2.0\n'
'==================================\n'
'\n'
'1. Definitions\n'
'--------------\n'
'\n'
'1.1. "Contributor"\n'
'    means each individual or legal entity that creates, contributes to\n'
'    the creation of, or owns Covered Software.\n'
'\n'
'1.2. "Contributor Version"\n'
'    means the combination of the Contributions of others (if any) used\n'
'    by a Contributor and that particular Contributor\'s Contribution.\n'
'\n'
'1.3. "Contribution"\n'
'    means Covered Software of a particular Contributor.\n'
'\n'
'1.4. "Covered Software"\n'
'    means Source Code Form to which the initial Contributor has attached\n'
'    the notice in Exhibit A, the Executable Form of such Source Code\n'
'    Form, and Modifications of such Source Code Form, in each case\n'
'    including portions thereof.\n'
'\n'
'1.5. "Incompatible With Secondary Licenses"\n'
'    means\n'
'\n'
'    (a) that the initial Contributor has attached the notice described\n'
'        in Exhibit B to the Covered Software; or\n'
'\n'
'    (b) that the Covered Software was made available under the terms of\n'
'        version 1.1 or earlier of the License, but not also under the\n'
'        terms of a Secondary License.\n'
'\n'
'1.6. "Executable Form"\n'
'    means any form of the work other than Source Code Form.\n'
'\n'
'1.7. "Larger Work"\n'
'    means a work that combines Covered Software with other material, in\n'
'    a separate file or files, that is not Covered Software.\n'
'\n'
'1.8. "License"\n'
'    means this document.\n'
'\n'
'1.9. "Licensable"\n'
'    means having the right to grant, to the maximum extent possible,\n'
'    whether at the time of the initial grant or subsequently, any and\n'
'    all of the rights conveyed by this License.\n'
'\n'
'1.10. "Modifications"\n'
'    means any of the following:\n'
'\n'
'    (a) any file in Source Code Form that results from an addition to,\n'
'        deletion from, or modification of the contents of Covered\n'
'        Software; or\n'
'\n'
'    (b) any new file in Source Code Form that contains any Covered\n'
'        Software.\n'
'\n'
'1.11. "Patent Claims" of a Contributor\n'
'    means any patent claim(s), including without limitation, method,\n'
'    process, and apparatus claims, in any patent Licensable by such\n'
'    Contributor that would be infringed, but for the grant of the\n'
'    License, by the making, using, selling, offering for sale, having\n'
'    made, import, or transfer of either its Contributions or its\n'
'    Contributor Version.\n'
'\n'
'1.12. "Secondary License"\n'
'    means either the GNU General Public License, Version 2.0, the GNU\n'
'    Lesser General Public License, Version 2.1, the GNU Affero General\n'
'    Public License, Version 3.0, or any later versions of those\n'
'    licenses.\n'
'\n'
'1.13. "Source Code Form"\n'
'    means the form of the work preferred for making modifications.\n'
'\n'
'1.14. "You" (or "Your")\n'
'    means an individual or a legal entity exercising rights under this\n'
'    License. For legal entities, "You" includes any entity that\n'
'    controls, is controlled by, or is under common control with You. For\n'
'    purposes of this definition, "control" means (a) the power, direct\n'
'    or indirect, to cause the direction or management of such entity,\n'
'    whether by contract or otherwise, or (b) ownership of more than\n'
'    fifty percent (50%) of the outstanding shares or beneficial\n'
'    ownership of such entity.\n'
'\n'
'2. License Grants and Conditions\n'
'--------------------------------\n'
'\n'
'2.1. Grants\n'
'\n'
'Each Contributor hereby grants You a world-wide, royalty-free,\n'
'non-exclusive license:\n'
'\n'
'(a) under intellectual property rights (other than patent or trademark)\n'
'    Licensable by such Contributor to use, reproduce, make available,\n'
'    modify, display, perform, distribute, and otherwise exploit its\n'
'    Contributions, either on an unmodified basis, with Modifications, or\n'
'    as part of a Larger Work; and\n'
'\n'
'(b) under Patent Claims of such Contributor to make, use, sell, offer\n'
'    for sale, have made, import, and otherwise transfer either its\n'
'    Contributions or its Contributor Version.\n'
'\n'
'2.2. Effective Date\n'
'\n'
'The licenses granted in Section 2.1 with respect to any Contribution\n'
'become effective for each Contribution on the date the Contributor first\n'
'distributes such Contribution.\n'
'\n'
'2.3. Limitations on Grant Scope\n'
'\n'
'The licenses granted in this Section 2 are the only rights granted under\n'
'this License. No additional rights or licenses will be implied from the\n'
'distribution or licensing of Covered Software under this License.\n'
'Notwithstanding Section 2.1(b) above, no patent license is granted by a\n'
'Contributor:\n'
'\n'
'(a) for any code that a Contributor has removed from Covered Software;\n'
'    or\n'
'\n'
'(b) for infringements caused by: (i) Your and any other third party\'s\n'
'    modifications of Covered Software, or (ii) the combination of its\n'
'    Contributions with other software (except as part of its Contributor\n'
'    Version); or\n'
'\n'
'(c) under Patent Claims infringed by Covered Software in the absence of\n'
'    its Contributions.\n'
'\n'
'This License does not grant any rights in the trademarks, service marks,\n'
'or logos of any Contributor (except as may be necessary to comply with\n'
'the notice requirements in Section 3.4).\n'
'\n'
'2.4. Subsequent Licenses\n'
'\n'
'No Contributor makes additional grants as a result of Your choice to\n'
'distribute the Covered Software under a subsequent version of this\n'
'License (see Section 10.2) or under the terms of a Secondary License (if\n'
'permitted under the terms of Section 3.3).\n'
'\n'
'2.5. Representation\n'
'\n'
'Each Contributor represents that the Contributor believes its\n'
'Contributions are its original creation(s) or it has sufficient rights\n'
'to grant the rights to its Contributions conveyed by this License.\n'
'\n'
'2.6. Fair Use\n'
'\n'
'This License is not intended to limit any rights You have under\n'
'applicable copyright doctrines of fair use, fair dealing, or other\n'
'equivalents.\n'
'\n'
'2.7. Conditions\n'
'\n'
'Sections 3.1, 3.2, 3.3, and 3.4 are conditions of the licenses granted\n'
'in Section 2.1.\n'
'\n'
'3. Responsibilities\n'
'-------------------\n'
'\n'
'3.1. Distribution of Source Form\n'
'\n'
'All distribution of Covered Software in Source Code Form, including any\n'
'Modifications that You create or to which You contribute, must be under\n'
'the terms of this License. You must inform recipients that the Source\n'
'Code Form of the Covered Software is governed by the terms of this\n'
'License, and how they can obtain a copy of this License. You may not\n'
'attempt to alter or restrict the recipients\' rights in the Source Code\n'
'Form.\n'
'\n'
'3.2. Distribution of Executable Form\n'
'\n'
'If You distribute Covered Software in Executable Form then:\n'
'\n'
'(a) such Covered Software must also be made available in Source Code\n'
'    Form, as described in Section 3.1, and You must inform recipients of\n'
'    the Executable Form how they can obtain a copy of such Source Code\n'
'    Form by reasonable means in a timely manner, at a charge no more\n'
'    than the cost of distribution to the recipient; and\n'
'\n'
'(b) You may distribute such Executable Form under the terms of this\n'
'    License, or sublicense it under different terms, provided that the\n'
'    license for the Executable Form does not attempt to limit or alter\n'
'    the recipients\' rights in the Source Code Form under this License.\n'
'\n'
'3.3. Distribution of a Larger Work\n'
'\n'
'You may create and distribute a Larger Work under terms of Your choice,\n'
'provided that You also comply with the requirements of this License for\n'
'the Covered Software. If the Larger Work is a combination of Covered\n'
'Software with a work governed by one or more Secondary Licenses, and the\n'
'Covered Software is not Incompatible With Secondary Licenses, this\n'
'License permits You to additionally distribute such Covered Software\n'
'under the terms of such Secondary License(s), so that the recipient of\n'
'the Larger Work may, at their option, further distribute the Covered\n'
'Software under the terms of either this License or such Secondary\n'
'License(s).\n'
'\n'
'3.4. Notices\n'
'\n'
'You may not remove or alter the substance of any license notices\n'
'(including copyright notices, patent notices, disclaimers of warranty,\n'
'or limitations of liability) contained within the Source Code Form of\n'
'the Covered Software, except that You may alter any license notices to\n'
'the extent required to remedy known factual inaccuracies.\n'
'\n'
'3.5. Application of Additional Terms\n'
'\n'
'You may choose to offer, and to charge a fee for, warranty, support,\n'
'indemnity or liability obligations to one or more recipients of Covered\n'
'Software. However, You may do so only on Your own behalf, and not on\n'
'behalf of any Contributor. You must make it absolutely clear that any\n'
'such warranty, support, indemnity, or liability obligation is offered by\n'
'You alone, and You hereby agree to indemnify every Contributor for any\n'
'liability incurred by such Contributor as a result of warranty, support,\n'
'indemnity or liability terms You offer. You may include additional\n'
'disclaimers of warranty and limitations of liability specific to any\n'
'jurisdiction.\n'
'\n'
'4. Inability to Comply Due to Statute or Regulation\n'
'---------------------------------------------------\n'
'\n'
'If it is impossible for You to comply with any of the terms of this\n'
'License with respect to some or all of the Covered Software due to\n'
'statute, judicial order, or regulation then You must: (a) comply with\n'
'the terms of this License to the maximum extent possible; and (b)\n'
'describe the limitations and the code they affect. Such description must\n'
'be placed in a text file included with all distributions of the Covered\n'
'Software under this License. Except to the extent prohibited by statute\n'
'or regulation, such description must be sufficiently detailed for a\n'
'recipient of ordinary skill to be able to understand it.\n'
'\n'
'5. Termination\n'
'--------------\n'
'\n'
'5.1. The rights granted under this License will terminate automatically\n'
'if You fail to comply with any of its terms. However, if You become\n'
'compliant, then the rights granted under this License from a particular\n'
'Contributor are reinstated (a) provisionally, unless and until such\n'
'Contributor explicitly and finally terminates Your grants, and (b) on an\n'
'ongoing basis, if such Contributor fails to notify You of the\n'
'non-compliance by some reasonable means prior to 60 days after You have\n'
'come back into compliance. Moreover, Your grants from a particular\n'
'Contributor are reinstated on an ongoing basis if such Contributor\n'
'notifies You of the non-compliance by some reasonable means, this is the\n'
'first time You have received notice of non-compliance with this License\n'
'from such Contributor, and You become compliant prior to 30 days after\n'
'Your receipt of the notice.\n'
'\n'
'5.2. If You initiate litigation against any entity by asserting a patent\n'
'infringement claim (excluding declaratory judgment actions,\n'
'counter-claims, and cross-claims) alleging that a Contributor Version\n'
'directly or indirectly infringes any patent, then the rights granted to\n'
'You by any and all Contributors for the Covered Software under Section\n'
'2.1 of this License shall terminate.\n'
'\n'
'5.3. In the event of termination under Sections 5.1 or 5.2 above, all\n'
'end user license agreements (excluding distributors and resellers) which\n'
'have been validly granted by You or Your distributors under this License\n'
'prior to termination shall survive termination.\n'
'\n'
'************************************************************************\n'
'*                                                                      *\n'
'*  6. Disclaimer of Warranty                                           *\n'
'*  -------------------------                                           *\n'
'*                                                                      *\n'
'*  Covered Software is provided under this License on an "as is"       *\n'
'*  basis, without warranty of any kind, either expressed, implied, or  *\n'
'*  statutory, including, without limitation, warranties that the       *\n'
'*  Covered Software is free of defects, merchantable, fit for a        *\n'
'*  particular purpose or non-infringing. The entire risk as to the     *\n'
'*  quality and performance of the Covered Software is with You.        *\n'
'*  Should any Covered Software prove defective in any respect, You     *\n'
'*  (not any Contributor) assume the cost of any necessary servicing,   *\n'
'*  repair, or correction. This disclaimer of warranty constitutes an   *\n'
'*  essential part of this License. No use of any Covered Software is   *\n'
'*  authorized under this License except under this disclaimer.         *\n'
'*                                                                      *\n'
'************************************************************************\n'
'\n'
'************************************************************************\n'
'*                                                                      *\n'
'*  7. Limitation of Liability                                          *\n'
'*  --------------------------                                          *\n'
'*                                                                      *\n'
'*  Under no circumstances and under no legal theory, whether tort      *\n'
'*  (including negligence), contract, or otherwise, shall any           *\n'
'*  Contributor, or anyone who distributes Covered Software as          *\n'
'*  permitted above, be liable to You for any direct, indirect,         *\n'
'*  special, incidental, or consequential damages of any character      *\n'
'*  including, without limitation, damages for lost profits, loss of    *\n'
'*  goodwill, work stoppage, computer failure or malfunction, or any    *\n'
'*  and all other commercial damages or losses, even if such party      *\n'
'*  shall have been informed of the possibility of such damages. This   *\n'
'*  limitation of liability shall not apply to liability for death or   *\n'
'*  personal injury resulting from such party\'s negligence to the       *\n'
'*  extent applicable law prohibits such limitation. Some               *\n'
'*  jurisdictions do not allow the exclusion or limitation of           *\n'
'*  incidental or consequential damages, so this exclusion and          *\n'
'*  limitation may not apply to You.                                    *\n'
'*                                                                      *\n'
'************************************************************************\n'
'\n'
'8. Litigation\n'
'-------------\n'
'\n'
'Any litigation relating to this License may be brought only in the\n'
'courts of a jurisdiction where the defendant maintains its principal\n'
'place of business and such litigation shall be governed by laws of that\n'
'jurisdiction, without reference to its conflict-of-law provisions.\n'
'Nothing in this Section shall prevent a party\'s ability to bring\n'
'cross-claims or counter-claims.\n'
'\n'
'9. Miscellaneous\n'
'----------------\n'
'\n'
'This License represents the complete agreement concerning the subject\n'
'matter hereof. If any provision of this License is held to be\n'
'unenforceable, such provision shall be reformed only to the extent\n'
'necessary to make it enforceable. Any law or regulation which provides\n'
'that the language of a contract shall be construed against the drafter\n'
'shall not be used to construe this License against a Contributor.\n'
'\n'
'10. Versions of the License\n'
'---------------------------\n'
'\n'
'10.1. New Versions\n'
'\n'
'Mozilla Foundation is the license steward. Except as provided in Section\n'
'10.3, no one other than the license steward has the right to modify or\n'
'publish new versions of this License. Each version will be given a\n'
'distinguishing version number.\n'
'\n'
'10.2. Effect of New Versions\n'
'\n'
'You may distribute the Covered Software under the terms of the version\n'
'of the License under which You originally received the Covered Software,\n'
'or under the terms of any subsequent version published by the license\n'
'steward.\n'
'\n'
'10.3. Modified Versions\n'
'\n'
'If you create software not governed by this License, and you want to\n'
'create a new license for such software, you may create and use a\n'
'modified version of this License if you rename the license and remove\n'
'any references to the name of the license steward (except to note that\n'
'such modified license differs from this License).\n'
'\n'
'10.4. Distributing Source Code Form that is Incompatible With Secondary\n'
'Licenses\n'
'\n'
'If You choose to distribute Source Code Form that is Incompatible With\n'
'Secondary Licenses under the terms of this version of the License, the\n'
'notice described in Exhibit B of this License must be attached.\n'
'\n'
'Exhibit A - Source Code Form License Notice\n'
'-------------------------------------------\n'
'\n'
'  This Source Code Form is subject to the terms of the Mozilla Public\n'
'  License, v. 2.0. If a copy of the MPL was not distributed with this\n'
'  file, You can obtain one at http://mozilla.org/MPL/2.0/.\n'
'\n'
'If it is not possible or desirable to put the notice in a particular\n'
'file, then You may include the notice in a location (such as a LICENSE\n'
'file in a relevant directory) where a recipient would be likely to look\n'
'for such a notice.\n'
'\n'
'You may add additional accurate notices of copyright ownership.\n'
'\n'
'Exhibit B - "Incompatible With Secondary Licenses" Notice\n'
'---------------------------------------------------------\n'
'\n'
'  This Source Code Form is "Incompatible With Secondary Licenses", as\n'
'  defined by the Mozilla Public License, v. 2.0.\n'
'\n'
)