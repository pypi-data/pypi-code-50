from fontTools.feaLib.error import FeatureLibError
from fontTools.feaLib.lexer import Lexer, IncludingLexer, NonIncludingLexer
from fontTools.misc.encodingTools import getEncoding
from fontTools.misc.py23 import *
import fontTools.feaLib.ast as ast
import logging
import os
import re


log = logging.getLogger(__name__)


class Parser(object):
    extensions = {}
    ast = ast
    SS_FEATURE_TAGS = {"ss%02d" % i for i in range(1, 20+1)}
    CV_FEATURE_TAGS = {"cv%02d" % i for i in range(1, 99+1)}

    def __init__(self, featurefile, glyphNames=(), followIncludes=True,
                 **kwargs):
        """Initializes a Parser object.

        Note: the `glyphNames` iterable serves a double role to help distinguish
        glyph names from ranges in the presence of hyphens and to ensure that glyph
        names referenced in a feature file are actually part of a font's glyph set.
        If the iterable is left empty, no glyph name in glyph set checking takes
        place.
        """
        if "glyphMap" in kwargs:
            from fontTools.misc.loggingTools import deprecateArgument
            deprecateArgument("glyphMap", "use 'glyphNames' (iterable) instead")
            if glyphNames:
                raise TypeError("'glyphNames' and (deprecated) 'glyphMap' are "
                                "mutually exclusive")
            glyphNames = kwargs.pop("glyphMap")
        if kwargs:
            raise TypeError("unsupported keyword argument%s: %s"
                            % ("" if len(kwargs) == 1 else "s",
                               ", ".join(repr(k) for k in kwargs)))

        self.glyphNames_ = set(glyphNames)
        self.doc_ = self.ast.FeatureFile()
        self.anchors_ = SymbolTable()
        self.glyphclasses_ = SymbolTable()
        self.lookups_ = SymbolTable()
        self.valuerecords_ = SymbolTable()
        self.symbol_tables_ = {
            self.anchors_, self.valuerecords_
        }
        self.next_token_type_, self.next_token_ = (None, None)
        self.cur_comments_ = []
        self.next_token_location_ = None
        lexerClass = IncludingLexer if followIncludes else NonIncludingLexer
        self.lexer_ = lexerClass(featurefile)
        self.advance_lexer_(comments=True)

    def parse(self):
        statements = self.doc_.statements
        while self.next_token_type_ is not None or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                statements.append(
                    self.ast.Comment(self.cur_token_,
                                     location=self.cur_token_location_))
            elif self.is_cur_keyword_("include"):
                statements.append(self.parse_include_())
            elif self.cur_token_type_ is Lexer.GLYPHCLASS:
                statements.append(self.parse_glyphclass_definition_())
            elif self.is_cur_keyword_(("anon", "anonymous")):
                statements.append(self.parse_anonymous_())
            elif self.is_cur_keyword_("anchorDef"):
                statements.append(self.parse_anchordef_())
            elif self.is_cur_keyword_("languagesystem"):
                statements.append(self.parse_languagesystem_())
            elif self.is_cur_keyword_("lookup"):
                statements.append(self.parse_lookup_(vertical=False))
            elif self.is_cur_keyword_("markClass"):
                statements.append(self.parse_markClass_())
            elif self.is_cur_keyword_("feature"):
                statements.append(self.parse_feature_block_())
            elif self.is_cur_keyword_("table"):
                statements.append(self.parse_table_())
            elif self.is_cur_keyword_("valueRecordDef"):
                statements.append(
                    self.parse_valuerecord_definition_(vertical=False))
            elif self.cur_token_type_ is Lexer.NAME and self.cur_token_ in self.extensions:
                statements.append(self.extensions[self.cur_token_](self))
            elif self.cur_token_type_ is Lexer.SYMBOL and self.cur_token_ == ";":
                continue
            else:
                raise FeatureLibError(
                    "Expected feature, languagesystem, lookup, markClass, "
                    "table, or glyph class definition, got {} \"{}\"".format(self.cur_token_type_, self.cur_token_),
                    self.cur_token_location_)
        return self.doc_

    def parse_anchor_(self):
        self.expect_symbol_("<")
        self.expect_keyword_("anchor")
        location = self.cur_token_location_

        if self.next_token_ == "NULL":
            self.expect_keyword_("NULL")
            self.expect_symbol_(">")
            return None

        if self.next_token_type_ == Lexer.NAME:
            name = self.expect_name_()
            anchordef = self.anchors_.resolve(name)
            if anchordef is None:
                raise FeatureLibError(
                    'Unknown anchor "%s"' % name,
                    self.cur_token_location_)
            self.expect_symbol_(">")
            return self.ast.Anchor(anchordef.x, anchordef.y,
                                   name=name,
                                   contourpoint=anchordef.contourpoint,
                                   xDeviceTable=None, yDeviceTable=None,
                                   location=location)

        x, y = self.expect_number_(), self.expect_number_()

        contourpoint = None
        if self.next_token_ == "contourpoint":
            self.expect_keyword_("contourpoint")
            contourpoint = self.expect_number_()

        if self.next_token_ == "<":
            xDeviceTable = self.parse_device_()
            yDeviceTable = self.parse_device_()
        else:
            xDeviceTable, yDeviceTable = None, None

        self.expect_symbol_(">")
        return self.ast.Anchor(x, y, name=None,
                               contourpoint=contourpoint,
                               xDeviceTable=xDeviceTable,
                               yDeviceTable=yDeviceTable,
                               location=location)

    def parse_anchor_marks_(self):
        """Parses a sequence of [<anchor> mark @MARKCLASS]*."""
        anchorMarks = []  # [(self.ast.Anchor, markClassName)*]
        while self.next_token_ == "<":
            anchor = self.parse_anchor_()
            if anchor is None and self.next_token_ != "mark":
                continue  # <anchor NULL> without mark, eg. in GPOS type 5
            self.expect_keyword_("mark")
            markClass = self.expect_markClass_reference_()
            anchorMarks.append((anchor, markClass))
        return anchorMarks

    def parse_anchordef_(self):
        assert self.is_cur_keyword_("anchorDef")
        location = self.cur_token_location_
        x, y = self.expect_number_(), self.expect_number_()
        contourpoint = None
        if self.next_token_ == "contourpoint":
            self.expect_keyword_("contourpoint")
            contourpoint = self.expect_number_()
        name = self.expect_name_()
        self.expect_symbol_(";")
        anchordef = self.ast.AnchorDefinition(name, x, y,
                                              contourpoint=contourpoint,
                                              location=location)
        self.anchors_.define(name, anchordef)
        return anchordef

    def parse_anonymous_(self):
        assert self.is_cur_keyword_(("anon", "anonymous"))
        tag = self.expect_tag_()
        _, content, location = self.lexer_.scan_anonymous_block(tag)
        self.advance_lexer_()
        self.expect_symbol_('}')
        end_tag = self.expect_tag_()
        assert tag == end_tag, "bad splitting in Lexer.scan_anonymous_block()"
        self.expect_symbol_(';')
        return self.ast.AnonymousBlock(tag, content, location=location)

    def parse_attach_(self):
        assert self.is_cur_keyword_("Attach")
        location = self.cur_token_location_
        glyphs = self.parse_glyphclass_(accept_glyphname=True)
        contourPoints = {self.expect_number_()}
        while self.next_token_ != ";":
            contourPoints.add(self.expect_number_())
        self.expect_symbol_(";")
        return self.ast.AttachStatement(glyphs, contourPoints,
                                        location=location)

    def parse_enumerate_(self, vertical):
        assert self.cur_token_ in {"enumerate", "enum"}
        self.advance_lexer_()
        return self.parse_position_(enumerated=True, vertical=vertical)

    def parse_GlyphClassDef_(self):
        """Parses 'GlyphClassDef @BASE, @LIGATURES, @MARKS, @COMPONENTS;'"""
        assert self.is_cur_keyword_("GlyphClassDef")
        location = self.cur_token_location_
        if self.next_token_ != ",":
            baseGlyphs = self.parse_glyphclass_(accept_glyphname=False)
        else:
            baseGlyphs = None
        self.expect_symbol_(",")
        if self.next_token_ != ",":
            ligatureGlyphs = self.parse_glyphclass_(accept_glyphname=False)
        else:
            ligatureGlyphs = None
        self.expect_symbol_(",")
        if self.next_token_ != ",":
            markGlyphs = self.parse_glyphclass_(accept_glyphname=False)
        else:
            markGlyphs = None
        self.expect_symbol_(",")
        if self.next_token_ != ";":
            componentGlyphs = self.parse_glyphclass_(accept_glyphname=False)
        else:
            componentGlyphs = None
        self.expect_symbol_(";")
        return self.ast.GlyphClassDefStatement(baseGlyphs, markGlyphs,
                                               ligatureGlyphs, componentGlyphs,
                                               location=location)

    def parse_glyphclass_definition_(self):
        """Parses glyph class definitions such as '@UPPERCASE = [A-Z];'"""
        location, name = self.cur_token_location_, self.cur_token_
        self.expect_symbol_("=")
        glyphs = self.parse_glyphclass_(accept_glyphname=False)
        self.expect_symbol_(";")
        glyphclass = self.ast.GlyphClassDefinition(name, glyphs,
                                                   location=location)
        self.glyphclasses_.define(name, glyphclass)
        return glyphclass

    def split_glyph_range_(self, name, location):
        # Since v1.20, the OpenType Feature File specification allows
        # for dashes in glyph names. A sequence like "a-b-c-d" could
        # therefore mean a single glyph whose name happens to be
        # "a-b-c-d", or it could mean a range from glyph "a" to glyph
        # "b-c-d", or a range from glyph "a-b" to glyph "c-d", or a
        # range from glyph "a-b-c" to glyph "d".Technically, this
        # example could be resolved because the (pretty complex)
        # definition of glyph ranges renders most of these splits
        # invalid. But the specification does not say that a compiler
        # should try to apply such fancy heuristics. To encourage
        # unambiguous feature files, we therefore try all possible
        # splits and reject the feature file if there are multiple
        # splits possible. It is intentional that we don't just emit a
        # warning; warnings tend to get ignored. To fix the problem,
        # font designers can trivially add spaces around the intended
        # split point, and we emit a compiler error that suggests
        # how exactly the source should be rewritten to make things
        # unambiguous.
        parts = name.split("-")
        solutions = []
        for i in range(len(parts)):
            start, limit = "-".join(parts[0:i]), "-".join(parts[i:])
            if start in self.glyphNames_ and limit in self.glyphNames_:
                solutions.append((start, limit))
        if len(solutions) == 1:
            start, limit = solutions[0]
            return start, limit
        elif len(solutions) == 0:
            raise FeatureLibError(
                "\"%s\" is not a glyph in the font, and it can not be split "
                "into a range of known glyphs" % name, location)
        else:
            ranges = " or ".join(["\"%s - %s\"" % (s, l) for s, l in solutions])
            raise FeatureLibError(
                "Ambiguous glyph range \"%s\"; "
                "please use %s to clarify what you mean" % (name, ranges),
                location)

    def parse_glyphclass_(self, accept_glyphname):
        if (accept_glyphname and
                self.next_token_type_ in (Lexer.NAME, Lexer.CID)):
            glyph = self.expect_glyph_()
            self.check_glyph_name_in_glyph_set(glyph)
            return self.ast.GlyphName(glyph, location=self.cur_token_location_)
        if self.next_token_type_ is Lexer.GLYPHCLASS:
            self.advance_lexer_()
            gc = self.glyphclasses_.resolve(self.cur_token_)
            if gc is None:
                raise FeatureLibError(
                    "Unknown glyph class @%s" % self.cur_token_,
                    self.cur_token_location_)
            if isinstance(gc, self.ast.MarkClass):
                return self.ast.MarkClassName(
                    gc, location=self.cur_token_location_)
            else:
                return self.ast.GlyphClassName(
                    gc, location=self.cur_token_location_)

        self.expect_symbol_("[")
        location = self.cur_token_location_
        glyphs = self.ast.GlyphClass(location=location)
        while self.next_token_ != "]":
            if self.next_token_type_ is Lexer.NAME:
                glyph = self.expect_glyph_()
                location = self.cur_token_location_
                if '-' in glyph and glyph not in self.glyphNames_:
                    start, limit = self.split_glyph_range_(glyph, location)
                    self.check_glyph_name_in_glyph_set(start, limit)
                    glyphs.add_range(
                        start, limit,
                        self.make_glyph_range_(location, start, limit))
                elif self.next_token_ == "-":
                    start = glyph
                    self.expect_symbol_("-")
                    limit = self.expect_glyph_()
                    self.check_glyph_name_in_glyph_set(start, limit)
                    glyphs.add_range(
                        start, limit,
                        self.make_glyph_range_(location, start, limit))
                else:
                    self.check_glyph_name_in_glyph_set(glyph)
                    glyphs.append(glyph)
            elif self.next_token_type_ is Lexer.CID:
                glyph = self.expect_glyph_()
                if self.next_token_ == "-":
                    range_location = self.cur_token_location_
                    range_start = self.cur_token_
                    self.expect_symbol_("-")
                    range_end = self.expect_cid_()
                    self.check_glyph_name_in_glyph_set(
                        f"cid{range_start:05d}",
                        f"cid{range_end:05d}",
                    )
                    glyphs.add_cid_range(range_start, range_end,
                                         self.make_cid_range_(range_location,
                                                              range_start, range_end))
                else:
                    glyph_name = f"cid{self.cur_token_:05d}"
                    self.check_glyph_name_in_glyph_set(glyph_name)
                    glyphs.append(glyph_name)
            elif self.next_token_type_ is Lexer.GLYPHCLASS:
                self.advance_lexer_()
                gc = self.glyphclasses_.resolve(self.cur_token_)
                if gc is None:
                    raise FeatureLibError(
                        "Unknown glyph class @%s" % self.cur_token_,
                        self.cur_token_location_)
                if isinstance(gc, self.ast.MarkClass):
                    gc = self.ast.MarkClassName(
                        gc, location=self.cur_token_location_)
                else:
                    gc = self.ast.GlyphClassName(
                        gc, location=self.cur_token_location_)
                glyphs.add_class(gc)
            else:
                raise FeatureLibError(
                    "Expected glyph name, glyph range, "
                    "or glyph class reference",
                    self.next_token_location_)
        self.expect_symbol_("]")
        return glyphs

    def parse_class_name_(self):
        name = self.expect_class_name_()
        gc = self.glyphclasses_.resolve(name)
        if gc is None:
            raise FeatureLibError(
                "Unknown glyph class @%s" % name,
                self.cur_token_location_)
        if isinstance(gc, self.ast.MarkClass):
            return self.ast.MarkClassName(
                gc, location=self.cur_token_location_)
        else:
            return self.ast.GlyphClassName(
                gc, location=self.cur_token_location_)

    def parse_glyph_pattern_(self, vertical):
        prefix, glyphs, lookups, values, suffix = ([], [], [], [], [])
        hasMarks = False
        while self.next_token_ not in {"by", "from", ";", ","}:
            gc = self.parse_glyphclass_(accept_glyphname=True)
            marked = False
            if self.next_token_ == "'":
                self.expect_symbol_("'")
                hasMarks = marked = True
            if marked:
                if suffix:
                    # makeotf also reports this as an error, while FontForge
                    # silently inserts ' in all the intervening glyphs.
                    # https://github.com/fonttools/fonttools/pull/1096
                    raise FeatureLibError(
                        "Unsupported contextual target sequence: at most "
                        "one run of marked (') glyph/class names allowed",
                        self.cur_token_location_)
                glyphs.append(gc)
            elif glyphs:
                suffix.append(gc)
            else:
                prefix.append(gc)

            if self.is_next_value_():
                values.append(self.parse_valuerecord_(vertical))
            else:
                values.append(None)

            lookup = None
            if self.next_token_ == "lookup":
                self.expect_keyword_("lookup")
                if not marked:
                    raise FeatureLibError(
                        "Lookups can only follow marked glyphs",
                        self.cur_token_location_)
                lookup_name = self.expect_name_()
                lookup = self.lookups_.resolve(lookup_name)
                if lookup is None:
                    raise FeatureLibError(
                        'Unknown lookup "%s"' % lookup_name,
                        self.cur_token_location_)
            if marked:
                lookups.append(lookup)

        if not glyphs and not suffix:  # eg., "sub f f i by"
            assert lookups == []
            return ([], prefix, [None] * len(prefix), values, [], hasMarks)
        else:
            assert not any(values[:len(prefix)]), values
            format1 = values[len(prefix):][:len(glyphs)]
            format2 = values[(len(prefix) + len(glyphs)):][:len(suffix)]
            values = format2 if format2 and isinstance(format2[0], self.ast.ValueRecord) else format1
            return (prefix, glyphs, lookups, values, suffix, hasMarks)

    def parse_chain_context_(self):
        location = self.cur_token_location_
        prefix, glyphs, lookups, values, suffix, hasMarks = \
            self.parse_glyph_pattern_(vertical=False)
        chainContext = [(prefix, glyphs, suffix)]
        hasLookups = any(lookups)
        while self.next_token_ == ",":
            self.expect_symbol_(",")
            prefix, glyphs, lookups, values, suffix, hasMarks = \
                self.parse_glyph_pattern_(vertical=False)
            chainContext.append((prefix, glyphs, suffix))
            hasLookups = hasLookups or any(lookups)
        self.expect_symbol_(";")
        return chainContext, hasLookups

    def parse_ignore_(self):
        assert self.is_cur_keyword_("ignore")
        location = self.cur_token_location_
        self.advance_lexer_()
        if self.cur_token_ in ["substitute", "sub"]:
            chainContext, hasLookups = self.parse_chain_context_()
            if hasLookups:
                raise FeatureLibError(
                    "No lookups can be specified for \"ignore sub\"",
                    location)
            return self.ast.IgnoreSubstStatement(chainContext,
                                                 location=location)
        if self.cur_token_ in ["position", "pos"]:
            chainContext, hasLookups = self.parse_chain_context_()
            if hasLookups:
                raise FeatureLibError(
                    "No lookups can be specified for \"ignore pos\"",
                    location)
            return self.ast.IgnorePosStatement(chainContext,
                                               location=location)
        raise FeatureLibError(
            "Expected \"substitute\" or \"position\"",
            self.cur_token_location_)

    def parse_include_(self):
        assert self.cur_token_ == "include"
        location = self.cur_token_location_
        filename = self.expect_filename_()
        # self.expect_symbol_(";")
        return ast.IncludeStatement(filename, location=location)

    def parse_language_(self):
        assert self.is_cur_keyword_("language")
        location = self.cur_token_location_
        language = self.expect_language_tag_()
        include_default, required = (True, False)
        if self.next_token_ in {"exclude_dflt", "include_dflt"}:
            include_default = (self.expect_name_() == "include_dflt")
        if self.next_token_ == "required":
            self.expect_keyword_("required")
            required = True
        self.expect_symbol_(";")
        return self.ast.LanguageStatement(language,
                                          include_default, required,
                                          location=location)

    def parse_ligatureCaretByIndex_(self):
        assert self.is_cur_keyword_("LigatureCaretByIndex")
        location = self.cur_token_location_
        glyphs = self.parse_glyphclass_(accept_glyphname=True)
        carets = [self.expect_number_()]
        while self.next_token_ != ";":
            carets.append(self.expect_number_())
        self.expect_symbol_(";")
        return self.ast.LigatureCaretByIndexStatement(glyphs, carets,
                                                      location=location)

    def parse_ligatureCaretByPos_(self):
        assert self.is_cur_keyword_("LigatureCaretByPos")
        location = self.cur_token_location_
        glyphs = self.parse_glyphclass_(accept_glyphname=True)
        carets = [self.expect_number_()]
        while self.next_token_ != ";":
            carets.append(self.expect_number_())
        self.expect_symbol_(";")
        return self.ast.LigatureCaretByPosStatement(glyphs, carets,
                                                    location=location)

    def parse_lookup_(self, vertical):
        assert self.is_cur_keyword_("lookup")
        location, name = self.cur_token_location_, self.expect_name_()

        if self.next_token_ == ";":
            lookup = self.lookups_.resolve(name)
            if lookup is None:
                raise FeatureLibError("Unknown lookup \"%s\"" % name,
                                      self.cur_token_location_)
            self.expect_symbol_(";")
            return self.ast.LookupReferenceStatement(lookup,
                                                     location=location)

        use_extension = False
        if self.next_token_ == "useExtension":
            self.expect_keyword_("useExtension")
            use_extension = True

        block = self.ast.LookupBlock(name, use_extension, location=location)
        self.parse_block_(block, vertical)
        self.lookups_.define(name, block)
        return block

    def parse_lookupflag_(self):
        assert self.is_cur_keyword_("lookupflag")
        location = self.cur_token_location_

        # format B: "lookupflag 6;"
        if self.next_token_type_ == Lexer.NUMBER:
            value = self.expect_number_()
            self.expect_symbol_(";")
            return self.ast.LookupFlagStatement(value, location=location)

        # format A: "lookupflag RightToLeft MarkAttachmentType @M;"
        value_seen = False
        value, markAttachment, markFilteringSet = 0, None, None
        flags = {
            "RightToLeft": 1, "IgnoreBaseGlyphs": 2,
            "IgnoreLigatures": 4, "IgnoreMarks": 8
        }
        seen = set()
        while self.next_token_ != ";":
            if self.next_token_ in seen:
                raise FeatureLibError(
                    "%s can be specified only once" % self.next_token_,
                    self.next_token_location_)
            seen.add(self.next_token_)
            if self.next_token_ == "MarkAttachmentType":
                self.expect_keyword_("MarkAttachmentType")
                markAttachment = self.parse_class_name_()
            elif self.next_token_ == "UseMarkFilteringSet":
                self.expect_keyword_("UseMarkFilteringSet")
                markFilteringSet = self.parse_class_name_()
            elif self.next_token_ in flags:
                value_seen = True
                value = value | flags[self.expect_name_()]
            else:
                raise FeatureLibError(
                    '"%s" is not a recognized lookupflag' % self.next_token_,
                    self.next_token_location_)
        self.expect_symbol_(";")

        if not any([value_seen, markAttachment, markFilteringSet]):
            raise FeatureLibError(
                'lookupflag must have a value', self.next_token_location_)

        return self.ast.LookupFlagStatement(value,
                                            markAttachment=markAttachment,
                                            markFilteringSet=markFilteringSet,
                                            location=location)

    def parse_markClass_(self):
        assert self.is_cur_keyword_("markClass")
        location = self.cur_token_location_
        glyphs = self.parse_glyphclass_(accept_glyphname=True)
        anchor = self.parse_anchor_()
        name = self.expect_class_name_()
        self.expect_symbol_(";")
        markClass = self.doc_.markClasses.get(name)
        if markClass is None:
            markClass = self.ast.MarkClass(name)
            self.doc_.markClasses[name] = markClass
            self.glyphclasses_.define(name, markClass)
        mcdef = self.ast.MarkClassDefinition(markClass, anchor, glyphs,
                                             location=location)
        markClass.addDefinition(mcdef)
        return mcdef

    def parse_position_(self, enumerated, vertical):
        assert self.cur_token_ in {"position", "pos"}
        if self.next_token_ == "cursive":  # GPOS type 3
            return self.parse_position_cursive_(enumerated, vertical)
        elif self.next_token_ == "base":   # GPOS type 4
            return self.parse_position_base_(enumerated, vertical)
        elif self.next_token_ == "ligature":   # GPOS type 5
            return self.parse_position_ligature_(enumerated, vertical)
        elif self.next_token_ == "mark":   # GPOS type 6
            return self.parse_position_mark_(enumerated, vertical)

        location = self.cur_token_location_
        prefix, glyphs, lookups, values, suffix, hasMarks = \
            self.parse_glyph_pattern_(vertical)
        self.expect_symbol_(";")

        if any(lookups):
            # GPOS type 8: Chaining contextual positioning; explicit lookups
            if any(values):
                raise FeatureLibError(
                    "If \"lookup\" is present, no values must be specified",
                    location)
            return self.ast.ChainContextPosStatement(
                prefix, glyphs, suffix, lookups, location=location)

        # Pair positioning, format A: "pos V 10 A -10;"
        # Pair positioning, format B: "pos V A -20;"
        if not prefix and not suffix and len(glyphs) == 2 and not hasMarks:
            if values[0] is None:  # Format B: "pos V A -20;"
                values.reverse()
            return self.ast.PairPosStatement(
                glyphs[0], values[0], glyphs[1], values[1],
                enumerated=enumerated,
                location=location)

        if enumerated:
            raise FeatureLibError(
                '"enumerate" is only allowed with pair positionings', location)
        return self.ast.SinglePosStatement(list(zip(glyphs, values)),
                                           prefix, suffix, forceChain=hasMarks,
                                           location=location)

    def parse_position_cursive_(self, enumerated, vertical):
        location = self.cur_token_location_
        self.expect_keyword_("cursive")
        if enumerated:
            raise FeatureLibError(
                '"enumerate" is not allowed with '
                'cursive attachment positioning',
                location)
        glyphclass = self.parse_glyphclass_(accept_glyphname=True)
        entryAnchor = self.parse_anchor_()
        exitAnchor = self.parse_anchor_()
        self.expect_symbol_(";")
        return self.ast.CursivePosStatement(
            glyphclass, entryAnchor, exitAnchor, location=location)

    def parse_position_base_(self, enumerated, vertical):
        location = self.cur_token_location_
        self.expect_keyword_("base")
        if enumerated:
            raise FeatureLibError(
                '"enumerate" is not allowed with '
                'mark-to-base attachment positioning',
                location)
        base = self.parse_glyphclass_(accept_glyphname=True)
        marks = self.parse_anchor_marks_()
        self.expect_symbol_(";")
        return self.ast.MarkBasePosStatement(base, marks, location=location)

    def parse_position_ligature_(self, enumerated, vertical):
        location = self.cur_token_location_
        self.expect_keyword_("ligature")
        if enumerated:
            raise FeatureLibError(
                '"enumerate" is not allowed with '
                'mark-to-ligature attachment positioning',
                location)
        ligatures = self.parse_glyphclass_(accept_glyphname=True)
        marks = [self.parse_anchor_marks_()]
        while self.next_token_ == "ligComponent":
            self.expect_keyword_("ligComponent")
            marks.append(self.parse_anchor_marks_())
        self.expect_symbol_(";")
        return self.ast.MarkLigPosStatement(ligatures, marks, location=location)

    def parse_position_mark_(self, enumerated, vertical):
        location = self.cur_token_location_
        self.expect_keyword_("mark")
        if enumerated:
            raise FeatureLibError(
                '"enumerate" is not allowed with '
                'mark-to-mark attachment positioning',
                location)
        baseMarks = self.parse_glyphclass_(accept_glyphname=True)
        marks = self.parse_anchor_marks_()
        self.expect_symbol_(";")
        return self.ast.MarkMarkPosStatement(baseMarks, marks,
                                             location=location)

    def parse_script_(self):
        assert self.is_cur_keyword_("script")
        location, script = self.cur_token_location_, self.expect_script_tag_()
        self.expect_symbol_(";")
        return self.ast.ScriptStatement(script, location=location)

    def parse_substitute_(self):
        assert self.cur_token_ in {"substitute", "sub", "reversesub", "rsub"}
        location = self.cur_token_location_
        reverse = self.cur_token_ in {"reversesub", "rsub"}
        old_prefix, old, lookups, values, old_suffix, hasMarks = \
            self.parse_glyph_pattern_(vertical=False)
        if any(values):
            raise FeatureLibError(
                "Substitution statements cannot contain values", location)
        new = []
        if self.next_token_ == "by":
            keyword = self.expect_keyword_("by")
            while self.next_token_ != ";":
                gc = self.parse_glyphclass_(accept_glyphname=True)
                new.append(gc)
        elif self.next_token_ == "from":
            keyword = self.expect_keyword_("from")
            new = [self.parse_glyphclass_(accept_glyphname=False)]
        else:
            keyword = None
        self.expect_symbol_(";")
        if len(new) == 0 and not any(lookups):
            raise FeatureLibError(
                'Expected "by", "from" or explicit lookup references',
                self.cur_token_location_)

        # GSUB lookup type 3: Alternate substitution.
        # Format: "substitute a from [a.1 a.2 a.3];"
        if keyword == "from":
            if reverse:
                raise FeatureLibError(
                    'Reverse chaining substitutions do not support "from"',
                    location)
            if len(old) != 1 or len(old[0].glyphSet()) != 1:
                raise FeatureLibError(
                    'Expected a single glyph before "from"',
                    location)
            if len(new) != 1:
                raise FeatureLibError(
                    'Expected a single glyphclass after "from"',
                    location)
            return self.ast.AlternateSubstStatement(
                old_prefix, old[0], old_suffix, new[0], location=location)

        num_lookups = len([l for l in lookups if l is not None])

        # GSUB lookup type 1: Single substitution.
        # Format A: "substitute a by a.sc;"
        # Format B: "substitute [one.fitted one.oldstyle] by one;"
        # Format C: "substitute [a-d] by [A.sc-D.sc];"
        if (not reverse and len(old) == 1 and len(new) == 1 and
                num_lookups == 0):
            glyphs = list(old[0].glyphSet())
            replacements = list(new[0].glyphSet())
            if len(replacements) == 1:
                replacements = replacements * len(glyphs)
            if len(glyphs) != len(replacements):
                raise FeatureLibError(
                    'Expected a glyph class with %d elements after "by", '
                    'but found a glyph class with %d elements' %
                    (len(glyphs), len(replacements)), location)
            return self.ast.SingleSubstStatement(
                old, new,
                old_prefix, old_suffix,
                forceChain=hasMarks,
                location=location
            )

        # GSUB lookup type 2: Multiple substitution.
        # Format: "substitute f_f_i by f f i;"
        if (not reverse and
                len(old) == 1 and len(old[0].glyphSet()) == 1 and
                len(new) > 1 and max([len(n.glyphSet()) for n in new]) == 1 and
                num_lookups == 0):
            return self.ast.MultipleSubstStatement(
                old_prefix, tuple(old[0].glyphSet())[0], old_suffix,
                tuple([list(n.glyphSet())[0] for n in new]),
                forceChain=hasMarks, location=location)

        # GSUB lookup type 4: Ligature substitution.
        # Format: "substitute f f i by f_f_i;"
        if (not reverse and
                len(old) > 1 and len(new) == 1 and
                len(new[0].glyphSet()) == 1 and
                num_lookups == 0):
            return self.ast.LigatureSubstStatement(
                old_prefix, old, old_suffix,
                list(new[0].glyphSet())[0], forceChain=hasMarks,
                location=location)

        # GSUB lookup type 8: Reverse chaining substitution.
        if reverse:
            if len(old) != 1:
                raise FeatureLibError(
                    "In reverse chaining single substitutions, "
                    "only a single glyph or glyph class can be replaced",
                    location)
            if len(new) != 1:
                raise FeatureLibError(
                    'In reverse chaining single substitutions, '
                    'the replacement (after "by") must be a single glyph '
                    'or glyph class', location)
            if num_lookups != 0:
                raise FeatureLibError(
                    "Reverse chaining substitutions cannot call named lookups",
                    location)
            glyphs = sorted(list(old[0].glyphSet()))
            replacements = sorted(list(new[0].glyphSet()))
            if len(replacements) == 1:
                replacements = replacements * len(glyphs)
            if len(glyphs) != len(replacements):
                raise FeatureLibError(
                    'Expected a glyph class with %d elements after "by", '
                    'but found a glyph class with %d elements' %
                    (len(glyphs), len(replacements)), location)
            return self.ast.ReverseChainSingleSubstStatement(
                old_prefix, old_suffix, old, new, location=location)

        if len(old) > 1 and len(new) > 1:
            raise FeatureLibError(
                'Direct substitution of multiple glyphs by multiple glyphs '
                'is not supported',
                location)

        # GSUB lookup type 6: Chaining contextual substitution.
        assert len(new) == 0, new
        rule = self.ast.ChainContextSubstStatement(
            old_prefix, old, old_suffix, lookups, location=location)
        return rule

    def parse_subtable_(self):
        assert self.is_cur_keyword_("subtable")
        location = self.cur_token_location_
        self.expect_symbol_(";")
        return self.ast.SubtableStatement(location=location)

    def parse_size_parameters_(self):
        assert self.is_cur_keyword_("parameters")
        location = self.cur_token_location_
        DesignSize = self.expect_decipoint_()
        SubfamilyID = self.expect_number_()
        RangeStart = 0
        RangeEnd = 0
        if self.next_token_type_ in (Lexer.NUMBER, Lexer.FLOAT) or \
                SubfamilyID != 0:
            RangeStart = self.expect_decipoint_()
            RangeEnd = self.expect_decipoint_()

        self.expect_symbol_(";")
        return self.ast.SizeParameters(DesignSize, SubfamilyID,
                                       RangeStart, RangeEnd,
                                       location=location)

    def parse_size_menuname_(self):
        assert self.is_cur_keyword_("sizemenuname")
        location = self.cur_token_location_
        platformID, platEncID, langID, string = self.parse_name_()
        return self.ast.FeatureNameStatement("size", platformID,
                                             platEncID, langID, string,
                                             location=location)

    def parse_table_(self):
        assert self.is_cur_keyword_("table")
        location, name = self.cur_token_location_, self.expect_tag_()
        table = self.ast.TableBlock(name, location=location)
        self.expect_symbol_("{")
        handler = {
            "GDEF": self.parse_table_GDEF_,
            "head": self.parse_table_head_,
            "hhea": self.parse_table_hhea_,
            "vhea": self.parse_table_vhea_,
            "name": self.parse_table_name_,
            "BASE": self.parse_table_BASE_,
            "OS/2": self.parse_table_OS_2_,
        }.get(name)
        if handler:
            handler(table)
        else:
            raise FeatureLibError('"table %s" is not supported' % name.strip(),
                                  location)
        self.expect_symbol_("}")
        end_tag = self.expect_tag_()
        if end_tag != name:
            raise FeatureLibError('Expected "%s"' % name.strip(),
                                  self.cur_token_location_)
        self.expect_symbol_(";")
        return table

    def parse_table_GDEF_(self, table):
        statements = table.statements
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.is_cur_keyword_("Attach"):
                statements.append(self.parse_attach_())
            elif self.is_cur_keyword_("GlyphClassDef"):
                statements.append(self.parse_GlyphClassDef_())
            elif self.is_cur_keyword_("LigatureCaretByIndex"):
                statements.append(self.parse_ligatureCaretByIndex_())
            elif self.is_cur_keyword_("LigatureCaretByPos"):
                statements.append(self.parse_ligatureCaretByPos_())
            elif self.cur_token_ == ";":
                continue
            else:
                raise FeatureLibError(
                    "Expected Attach, LigatureCaretByIndex, "
                    "or LigatureCaretByPos",
                    self.cur_token_location_)

    def parse_table_head_(self, table):
        statements = table.statements
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.is_cur_keyword_("FontRevision"):
                statements.append(self.parse_FontRevision_())
            elif self.cur_token_ == ";":
                continue
            else:
                raise FeatureLibError("Expected FontRevision",
                                      self.cur_token_location_)

    def parse_table_hhea_(self, table):
        statements = table.statements
        fields = ("CaretOffset", "Ascender", "Descender", "LineGap")
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.cur_token_type_ is Lexer.NAME and self.cur_token_ in fields:
                key = self.cur_token_.lower()
                value = self.expect_number_()
                statements.append(
                    self.ast.HheaField(key, value,
                                       location=self.cur_token_location_))
                if self.next_token_ != ";":
                    raise FeatureLibError("Incomplete statement", self.next_token_location_)
            elif self.cur_token_ == ";":
                continue
            else:
                raise FeatureLibError("Expected CaretOffset, Ascender, "
                                      "Descender or LineGap",
                                      self.cur_token_location_)

    def parse_table_vhea_(self, table):
        statements = table.statements
        fields = ("VertTypoAscender", "VertTypoDescender", "VertTypoLineGap")
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.cur_token_type_ is Lexer.NAME and self.cur_token_ in fields:
                key = self.cur_token_.lower()
                value = self.expect_number_()
                statements.append(
                    self.ast.VheaField(key, value,
                                       location=self.cur_token_location_))
                if self.next_token_ != ";":
                    raise FeatureLibError("Incomplete statement", self.next_token_location_)
            elif self.cur_token_ == ";":
                continue
            else:
                raise FeatureLibError("Expected VertTypoAscender, "
                                      "VertTypoDescender or VertTypoLineGap",
                                      self.cur_token_location_)

    def parse_table_name_(self, table):
        statements = table.statements
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.is_cur_keyword_("nameid"):
                statement = self.parse_nameid_()
                if statement:
                    statements.append(statement)
            elif self.cur_token_ == ";":
                continue
            else:
                raise FeatureLibError("Expected nameid",
                                      self.cur_token_location_)

    def parse_name_(self):
        platEncID = None
        langID = None
        if self.next_token_type_ in Lexer.NUMBERS:
            platformID = self.expect_any_number_()
            location = self.cur_token_location_
            if platformID not in (1, 3):
                raise FeatureLibError("Expected platform id 1 or 3", location)
            if self.next_token_type_ in Lexer.NUMBERS:
                platEncID = self.expect_any_number_()
                langID = self.expect_any_number_()
        else:
            platformID = 3
            location = self.cur_token_location_

        if platformID == 1:                # Macintosh
            platEncID = platEncID or 0     # Roman
            langID = langID or 0           # English
        else:                              # 3, Windows
            platEncID = platEncID or 1     # Unicode
            langID = langID or 0x0409      # English

        string = self.expect_string_()
        self.expect_symbol_(";")

        encoding = getEncoding(platformID, platEncID, langID)
        if encoding is None:
            raise FeatureLibError("Unsupported encoding", location)
        unescaped = self.unescape_string_(string, encoding)
        return platformID, platEncID, langID, unescaped

    def parse_nameid_(self):
        assert self.cur_token_ == "nameid", self.cur_token_
        location, nameID = self.cur_token_location_, self.expect_any_number_()
        if nameID > 32767:
            raise FeatureLibError("Name id value cannot be greater than 32767",
                                  self.cur_token_location_)
        if 1 <= nameID <= 6:
            log.warning("Name id %d cannot be set from the feature file. "
                        "Ignoring record" % nameID)
            self.parse_name_()  # skip to the next record
            return None

        platformID, platEncID, langID, string = self.parse_name_()
        return self.ast.NameRecord(nameID, platformID, platEncID,
                                   langID, string, location=location)

    def unescape_string_(self, string, encoding):
        if encoding == "utf_16_be":
            s = re.sub(r"\\[0-9a-fA-F]{4}", self.unescape_unichr_, string)
        else:
            unescape = lambda m: self.unescape_byte_(m, encoding)
            s = re.sub(r"\\[0-9a-fA-F]{2}", unescape, string)
        # We now have a Unicode string, but it might contain surrogate pairs.
        # We convert surrogates to actual Unicode by round-tripping through
        # Python's UTF-16 codec in a special mode.
        utf16 = tobytes(s, "utf_16_be", "surrogatepass")
        return tounicode(utf16, "utf_16_be")

    @staticmethod
    def unescape_unichr_(match):
        n = match.group(0)[1:]
        return unichr(int(n, 16))

    @staticmethod
    def unescape_byte_(match, encoding):
        n = match.group(0)[1:]
        return bytechr(int(n, 16)).decode(encoding)

    def parse_table_BASE_(self, table):
        statements = table.statements
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.is_cur_keyword_("HorizAxis.BaseTagList"):
                horiz_bases = self.parse_base_tag_list_()
            elif self.is_cur_keyword_("HorizAxis.BaseScriptList"):
                horiz_scripts = self.parse_base_script_list_(len(horiz_bases))
                statements.append(
                        self.ast.BaseAxis(horiz_bases,
                                          horiz_scripts, False,
                                          location=self.cur_token_location_))
            elif self.is_cur_keyword_("VertAxis.BaseTagList"):
                vert_bases = self.parse_base_tag_list_()
            elif self.is_cur_keyword_("VertAxis.BaseScriptList"):
                vert_scripts = self.parse_base_script_list_(len(vert_bases))
                statements.append(
                        self.ast.BaseAxis(vert_bases,
                                          vert_scripts, True,
                                          location=self.cur_token_location_))
            elif self.cur_token_ == ";":
                continue

    def parse_table_OS_2_(self, table):
        statements = table.statements
        numbers = ("FSType", "TypoAscender", "TypoDescender", "TypoLineGap",
                   "winAscent", "winDescent", "XHeight", "CapHeight",
                   "WeightClass", "WidthClass", "LowerOpSize", "UpperOpSize")
        ranges = ("UnicodeRange", "CodePageRange")
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.cur_token_type_ is Lexer.NAME:
                key = self.cur_token_.lower()
                value = None
                if self.cur_token_ in numbers:
                    value = self.expect_number_()
                elif self.is_cur_keyword_("Panose"):
                    value = []
                    for i in range(10):
                        value.append(self.expect_number_())
                elif self.cur_token_ in ranges:
                    value = []
                    while self.next_token_ != ";":
                         value.append(self.expect_number_())
                elif self.is_cur_keyword_("Vendor"):
                    value = self.expect_string_()
                statements.append(
                    self.ast.OS2Field(key, value,
                                      location=self.cur_token_location_))
            elif self.cur_token_ == ";":
                continue

    def parse_base_tag_list_(self):
        assert self.cur_token_ in ("HorizAxis.BaseTagList",
                                   "VertAxis.BaseTagList"), self.cur_token_
        bases = []
        while self.next_token_ != ";":
            bases.append(self.expect_script_tag_())
        self.expect_symbol_(";")
        return bases

    def parse_base_script_list_(self, count):
        assert self.cur_token_ in ("HorizAxis.BaseScriptList",
                                   "VertAxis.BaseScriptList"), self.cur_token_
        scripts = [(self.parse_base_script_record_(count))]
        while self.next_token_ == ",":
            self.expect_symbol_(",")
            scripts.append(self.parse_base_script_record_(count))
        self.expect_symbol_(";")
        return scripts

    def parse_base_script_record_(self, count):
        script_tag = self.expect_script_tag_()
        base_tag = self.expect_script_tag_()
        coords = [self.expect_number_() for i in range(count)]
        return script_tag, base_tag, coords

    def parse_device_(self):
        result = None
        self.expect_symbol_("<")
        self.expect_keyword_("device")
        if self.next_token_ == "NULL":
            self.expect_keyword_("NULL")
        else:
            result = [(self.expect_number_(), self.expect_number_())]
            while self.next_token_ == ",":
                self.expect_symbol_(",")
                result.append((self.expect_number_(), self.expect_number_()))
            result = tuple(result)  # make it hashable
        self.expect_symbol_(">")
        return result

    def is_next_value_(self):
        return self.next_token_type_ is Lexer.NUMBER or self.next_token_ == "<"

    def parse_valuerecord_(self, vertical):
        if self.next_token_type_ is Lexer.NUMBER:
            number, location = self.expect_number_(), self.cur_token_location_
            if vertical:
                val = self.ast.ValueRecord(yAdvance=number,
                                           vertical=vertical,
                                           location=location)
            else:
                val = self.ast.ValueRecord(xAdvance=number,
                                           vertical=vertical,
                                           location=location)
            return val
        self.expect_symbol_("<")
        location = self.cur_token_location_
        if self.next_token_type_ is Lexer.NAME:
            name = self.expect_name_()
            if name == "NULL":
                self.expect_symbol_(">")
                return self.ast.ValueRecord()
            vrd = self.valuerecords_.resolve(name)
            if vrd is None:
                raise FeatureLibError("Unknown valueRecordDef \"%s\"" % name,
                                      self.cur_token_location_)
            value = vrd.value
            xPlacement, yPlacement = (value.xPlacement, value.yPlacement)
            xAdvance, yAdvance = (value.xAdvance, value.yAdvance)
        else:
            xPlacement, yPlacement, xAdvance, yAdvance = (
                self.expect_number_(), self.expect_number_(),
                self.expect_number_(), self.expect_number_())

        if self.next_token_ == "<":
            xPlaDevice, yPlaDevice, xAdvDevice, yAdvDevice = (
                self.parse_device_(), self.parse_device_(),
                self.parse_device_(), self.parse_device_())
            allDeltas = sorted([
                delta
                for size, delta
                in (xPlaDevice if xPlaDevice else ()) +
                (yPlaDevice if yPlaDevice else ()) +
                (xAdvDevice if xAdvDevice else ()) +
                (yAdvDevice if yAdvDevice else ())])
            if allDeltas[0] < -128 or allDeltas[-1] > 127:
                raise FeatureLibError(
                    "Device value out of valid range (-128..127)",
                    self.cur_token_location_)
        else:
            xPlaDevice, yPlaDevice, xAdvDevice, yAdvDevice = (
                None, None, None, None)

        self.expect_symbol_(">")
        return self.ast.ValueRecord(
            xPlacement, yPlacement, xAdvance, yAdvance,
            xPlaDevice, yPlaDevice, xAdvDevice, yAdvDevice,
            vertical=vertical, location=location)

    def parse_valuerecord_definition_(self, vertical):
        assert self.is_cur_keyword_("valueRecordDef")
        location = self.cur_token_location_
        value = self.parse_valuerecord_(vertical)
        name = self.expect_name_()
        self.expect_symbol_(";")
        vrd = self.ast.ValueRecordDefinition(name, value, location=location)
        self.valuerecords_.define(name, vrd)
        return vrd

    def parse_languagesystem_(self):
        assert self.cur_token_ == "languagesystem"
        location = self.cur_token_location_
        script = self.expect_script_tag_()
        language = self.expect_language_tag_()
        self.expect_symbol_(";")
        return self.ast.LanguageSystemStatement(script, language,
                                                location=location)

    def parse_feature_block_(self):
        assert self.cur_token_ == "feature"
        location = self.cur_token_location_
        tag = self.expect_tag_()
        vertical = (tag in {"vkrn", "vpal", "vhal", "valt"})

        stylisticset = None
        cv_feature = None
        size_feature = False
        if tag in self.SS_FEATURE_TAGS:
            stylisticset = tag
        elif tag in self.CV_FEATURE_TAGS:
            cv_feature = tag
        elif tag == "size":
            size_feature = True

        use_extension = False
        if self.next_token_ == "useExtension":
            self.expect_keyword_("useExtension")
            use_extension = True

        block = self.ast.FeatureBlock(tag, use_extension=use_extension,
                                      location=location)
        self.parse_block_(block, vertical, stylisticset, size_feature,
                          cv_feature)
        return block

    def parse_feature_reference_(self):
        assert self.cur_token_ == "feature", self.cur_token_
        location = self.cur_token_location_
        featureName = self.expect_tag_()
        self.expect_symbol_(";")
        return self.ast.FeatureReferenceStatement(featureName,
                                                  location=location)

    def parse_featureNames_(self, tag):
        assert self.cur_token_ == "featureNames", self.cur_token_
        block = self.ast.NestedBlock(tag, self.cur_token_,
                                     location=self.cur_token_location_)
        self.expect_symbol_("{")
        for symtab in self.symbol_tables_:
            symtab.enter_scope()
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                block.statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.is_cur_keyword_("name"):
                location = self.cur_token_location_
                platformID, platEncID, langID, string = self.parse_name_()
                block.statements.append(
                    self.ast.FeatureNameStatement(tag, platformID,
                                                  platEncID, langID, string,
                                                  location=location))
            elif self.cur_token_ == ";":
                continue
            else:
                raise FeatureLibError('Expected "name"',
                                      self.cur_token_location_)
        self.expect_symbol_("}")
        for symtab in self.symbol_tables_:
            symtab.exit_scope()
        self.expect_symbol_(";")
        return block

    def parse_cvParameters_(self, tag):
        assert self.cur_token_ == "cvParameters", self.cur_token_
        block = self.ast.NestedBlock(tag, self.cur_token_,
                                     location=self.cur_token_location_)
        self.expect_symbol_("{")
        for symtab in self.symbol_tables_:
            symtab.enter_scope()

        statements = block.statements
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.is_cur_keyword_({"FeatUILabelNameID",
                                       "FeatUITooltipTextNameID",
                                       "SampleTextNameID",
                                       "ParamUILabelNameID"}):
                statements.append(self.parse_cvNameIDs_(tag, self.cur_token_))
            elif self.is_cur_keyword_("Character"):
                statements.append(self.parse_cvCharacter_(tag))
            elif self.cur_token_ == ";":
                continue
            else:
                raise FeatureLibError(
                    "Expected statement: got {} {}".format(
                        self.cur_token_type_, self.cur_token_),
                    self.cur_token_location_)

        self.expect_symbol_("}")
        for symtab in self.symbol_tables_:
            symtab.exit_scope()
        self.expect_symbol_(";")
        return block

    def parse_cvNameIDs_(self, tag, block_name):
        assert self.cur_token_ == block_name, self.cur_token_
        block = self.ast.NestedBlock(tag, block_name,
                                     location=self.cur_token_location_)
        self.expect_symbol_("{")
        for symtab in self.symbol_tables_:
            symtab.enter_scope()
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                block.statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.is_cur_keyword_("name"):
                location = self.cur_token_location_
                platformID, platEncID, langID, string = self.parse_name_()
                block.statements.append(
                    self.ast.CVParametersNameStatement(
                        tag, platformID, platEncID, langID, string,
                        block_name, location=location))
            elif self.cur_token_ == ";":
                continue
            else:
                raise FeatureLibError('Expected "name"',
                                      self.cur_token_location_)
        self.expect_symbol_("}")
        for symtab in self.symbol_tables_:
            symtab.exit_scope()
        self.expect_symbol_(";")
        return block

    def parse_cvCharacter_(self, tag):
        assert self.cur_token_ == "Character", self.cur_token_
        location, character = self.cur_token_location_, self.expect_any_number_()
        self.expect_symbol_(";")
        if not (0xFFFFFF >= character >= 0):
            raise FeatureLibError("Character value must be between "
                                  "{:#x} and {:#x}".format(0, 0xFFFFFF),
                                  location)
        return self.ast.CharacterStatement(character, tag, location=location)

    def parse_FontRevision_(self):
        assert self.cur_token_ == "FontRevision", self.cur_token_
        location, version = self.cur_token_location_, self.expect_float_()
        self.expect_symbol_(";")
        if version <= 0:
            raise FeatureLibError("Font revision numbers must be positive",
                                  location)
        return self.ast.FontRevisionStatement(version, location=location)

    def parse_block_(self, block, vertical, stylisticset=None,
                     size_feature=False, cv_feature=None):
        self.expect_symbol_("{")
        for symtab in self.symbol_tables_:
            symtab.enter_scope()

        statements = block.statements
        while self.next_token_ != "}" or self.cur_comments_:
            self.advance_lexer_(comments=True)
            if self.cur_token_type_ is Lexer.COMMENT:
                statements.append(self.ast.Comment(
                    self.cur_token_, location=self.cur_token_location_))
            elif self.cur_token_type_ is Lexer.GLYPHCLASS:
                statements.append(self.parse_glyphclass_definition_())
            elif self.is_cur_keyword_("anchorDef"):
                statements.append(self.parse_anchordef_())
            elif self.is_cur_keyword_({"enum", "enumerate"}):
                statements.append(self.parse_enumerate_(vertical=vertical))
            elif self.is_cur_keyword_("feature"):
                statements.append(self.parse_feature_reference_())
            elif self.is_cur_keyword_("ignore"):
                statements.append(self.parse_ignore_())
            elif self.is_cur_keyword_("language"):
                statements.append(self.parse_language_())
            elif self.is_cur_keyword_("lookup"):
                statements.append(self.parse_lookup_(vertical))
            elif self.is_cur_keyword_("lookupflag"):
                statements.append(self.parse_lookupflag_())
            elif self.is_cur_keyword_("markClass"):
                statements.append(self.parse_markClass_())
            elif self.is_cur_keyword_({"pos", "position"}):
                statements.append(
                    self.parse_position_(enumerated=False, vertical=vertical))
            elif self.is_cur_keyword_("script"):
                statements.append(self.parse_script_())
            elif (self.is_cur_keyword_({"sub", "substitute",
                                        "rsub", "reversesub"})):
                statements.append(self.parse_substitute_())
            elif self.is_cur_keyword_("subtable"):
                statements.append(self.parse_subtable_())
            elif self.is_cur_keyword_("valueRecordDef"):
                statements.append(self.parse_valuerecord_definition_(vertical))
            elif stylisticset and self.is_cur_keyword_("featureNames"):
                statements.append(self.parse_featureNames_(stylisticset))
            elif cv_feature and self.is_cur_keyword_("cvParameters"):
                statements.append(self.parse_cvParameters_(cv_feature))
            elif size_feature and self.is_cur_keyword_("parameters"):
                statements.append(self.parse_size_parameters_())
            elif size_feature and self.is_cur_keyword_("sizemenuname"):
                statements.append(self.parse_size_menuname_())
            elif self.cur_token_type_ is Lexer.NAME and self.cur_token_ in self.extensions:
                statements.append(self.extensions[self.cur_token_](self))
            elif self.cur_token_ == ";":
                continue
            else:
                raise FeatureLibError(
                    "Expected glyph class definition or statement: got {} {}".format(self.cur_token_type_, self.cur_token_),
                    self.cur_token_location_)

        self.expect_symbol_("}")
        for symtab in self.symbol_tables_:
            symtab.exit_scope()

        name = self.expect_name_()
        if name != block.name.strip():
            raise FeatureLibError("Expected \"%s\"" % block.name.strip(),
                                  self.cur_token_location_)
        self.expect_symbol_(";")

        # A multiple substitution may have a single destination, in which case
        # it will look just like a single substitution. So if there are both
        # multiple and single substitutions, upgrade all the single ones to
        # multiple substitutions.

        # Check if we have a mix of non-contextual singles and multiples.
        has_single = False
        has_multiple = False
        for s in statements:
            if isinstance(s, self.ast.SingleSubstStatement):
                has_single = not any([s.prefix, s.suffix, s.forceChain])
            elif isinstance(s, self.ast.MultipleSubstStatement):
                has_multiple = not any([s.prefix, s.suffix, s.forceChain])

        # Upgrade all single substitutions to multiple substitutions.
        if has_single and has_multiple:
            statements = []
            for s in block.statements:
                if isinstance(s, self.ast.SingleSubstStatement):
                    glyphs = s.glyphs[0].glyphSet()
                    replacements = s.replacements[0].glyphSet()
                    if len(replacements) == 1:
                        replacements *= len(glyphs)
                    for i, glyph in enumerate(glyphs):
                        statements.append(
                            self.ast.MultipleSubstStatement(
                                s.prefix, glyph, s.suffix, [replacements[i]],
                                s.forceChain, location=s.location))
                else:
                    statements.append(s)
            block.statements = statements

    def is_cur_keyword_(self, k):
        if self.cur_token_type_ is Lexer.NAME:
            if isinstance(k, type("")):  # basestring is gone in Python3
                return self.cur_token_ == k
            else:
                return self.cur_token_ in k
        return False

    def expect_class_name_(self):
        self.advance_lexer_()
        if self.cur_token_type_ is not Lexer.GLYPHCLASS:
            raise FeatureLibError("Expected @NAME", self.cur_token_location_)
        return self.cur_token_

    def expect_cid_(self):
        self.advance_lexer_()
        if self.cur_token_type_ is Lexer.CID:
            return self.cur_token_
        raise FeatureLibError("Expected a CID", self.cur_token_location_)

    def expect_filename_(self):
        self.advance_lexer_()
        if self.cur_token_type_ is not Lexer.FILENAME:
            raise FeatureLibError("Expected file name",
                                  self.cur_token_location_)
        return self.cur_token_

    def expect_glyph_(self):
        self.advance_lexer_()
        if self.cur_token_type_ is Lexer.NAME:
            self.cur_token_ = self.cur_token_.lstrip("\\")
            if len(self.cur_token_) > 63:
                raise FeatureLibError(
                    "Glyph names must not be longer than 63 characters",
                    self.cur_token_location_)
            return self.cur_token_
        elif self.cur_token_type_ is Lexer.CID:
            return "cid%05d" % self.cur_token_
        raise FeatureLibError("Expected a glyph name or CID",
                              self.cur_token_location_)

    def check_glyph_name_in_glyph_set(self, *names):
        """Raises if glyph name (just `start`) or glyph names of a
        range (`start` and `end`) are not in the glyph set.

        If no glyph set is present, does nothing.
        """
        if self.glyphNames_:
            missing = [name for name in names if name not in self.glyphNames_]
            if missing:
                raise FeatureLibError(
                    "The following glyph names are referenced but are missing from the "
                    f"glyph set: {', '.join(missing)}",
                    self.cur_token_location_
                )

    def expect_markClass_reference_(self):
        name = self.expect_class_name_()
        mc = self.glyphclasses_.resolve(name)
        if mc is None:
            raise FeatureLibError("Unknown markClass @%s" % name,
                                  self.cur_token_location_)
        if not isinstance(mc, self.ast.MarkClass):
            raise FeatureLibError("@%s is not a markClass" % name,
                                  self.cur_token_location_)
        return mc

    def expect_tag_(self):
        self.advance_lexer_()
        if self.cur_token_type_ is not Lexer.NAME:
            raise FeatureLibError("Expected a tag", self.cur_token_location_)
        if len(self.cur_token_) > 4:
            raise FeatureLibError("Tags can not be longer than 4 characters",
                                  self.cur_token_location_)
        return (self.cur_token_ + "    ")[:4]

    def expect_script_tag_(self):
        tag = self.expect_tag_()
        if tag == "dflt":
            raise FeatureLibError(
                '"dflt" is not a valid script tag; use "DFLT" instead',
                self.cur_token_location_)
        return tag

    def expect_language_tag_(self):
        tag = self.expect_tag_()
        if tag == "DFLT":
            raise FeatureLibError(
                '"DFLT" is not a valid language tag; use "dflt" instead',
                self.cur_token_location_)
        return tag

    def expect_symbol_(self, symbol):
        self.advance_lexer_()
        if self.cur_token_type_ is Lexer.SYMBOL and self.cur_token_ == symbol:
            return symbol
        raise FeatureLibError("Expected '%s'" % symbol,
                              self.cur_token_location_)

    def expect_keyword_(self, keyword):
        self.advance_lexer_()
        if self.cur_token_type_ is Lexer.NAME and self.cur_token_ == keyword:
            return self.cur_token_
        raise FeatureLibError("Expected \"%s\"" % keyword,
                              self.cur_token_location_)

    def expect_name_(self):
        self.advance_lexer_()
        if self.cur_token_type_ is Lexer.NAME:
            return self.cur_token_
        raise FeatureLibError("Expected a name", self.cur_token_location_)

    def expect_number_(self):
        self.advance_lexer_()
        if self.cur_token_type_ is Lexer.NUMBER:
            return self.cur_token_
        raise FeatureLibError("Expected a number", self.cur_token_location_)

    def expect_any_number_(self):
        self.advance_lexer_()
        if self.cur_token_type_ in Lexer.NUMBERS:
            return self.cur_token_
        raise FeatureLibError("Expected a decimal, hexadecimal or octal number",
                              self.cur_token_location_)

    def expect_float_(self):
        self.advance_lexer_()
        if self.cur_token_type_ is Lexer.FLOAT:
            return self.cur_token_
        raise FeatureLibError("Expected a floating-point number",
                              self.cur_token_location_)

    def expect_decipoint_(self):
        if self.next_token_type_ == Lexer.FLOAT:
            return self.expect_float_()
        elif self.next_token_type_ is Lexer.NUMBER:
            return self.expect_number_() / 10
        else:
            raise FeatureLibError("Expected an integer or floating-point number",
                                  self.cur_token_location_)

    def expect_string_(self):
        self.advance_lexer_()
        if self.cur_token_type_ is Lexer.STRING:
            return self.cur_token_
        raise FeatureLibError("Expected a string", self.cur_token_location_)

    def advance_lexer_(self, comments=False):
        if comments and self.cur_comments_:
            self.cur_token_type_ = Lexer.COMMENT
            self.cur_token_, self.cur_token_location_ = self.cur_comments_.pop(0)
            return
        else:
            self.cur_token_type_, self.cur_token_, self.cur_token_location_ = (
                self.next_token_type_, self.next_token_, self.next_token_location_)
        while True:
            try:
                (self.next_token_type_, self.next_token_,
                 self.next_token_location_) = next(self.lexer_)
            except StopIteration:
                self.next_token_type_, self.next_token_ = (None, None)
            if self.next_token_type_ != Lexer.COMMENT:
                break
            self.cur_comments_.append((self.next_token_, self.next_token_location_))

    @staticmethod
    def reverse_string_(s):
        """'abc' --> 'cba'"""
        return ''.join(reversed(list(s)))

    def make_cid_range_(self, location, start, limit):
        """(location, 999, 1001) --> ["cid00999", "cid01000", "cid01001"]"""
        result = list()
        if start > limit:
            raise FeatureLibError(
                "Bad range: start should be less than limit", location)
        for cid in range(start, limit + 1):
            result.append("cid%05d" % cid)
        return result

    def make_glyph_range_(self, location, start, limit):
        """(location, "a.sc", "d.sc") --> ["a.sc", "b.sc", "c.sc", "d.sc"]"""
        result = list()
        if len(start) != len(limit):
            raise FeatureLibError(
                "Bad range: \"%s\" and \"%s\" should have the same length" %
                (start, limit), location)

        rev = self.reverse_string_
        prefix = os.path.commonprefix([start, limit])
        suffix = rev(os.path.commonprefix([rev(start), rev(limit)]))
        if len(suffix) > 0:
            start_range = start[len(prefix):-len(suffix)]
            limit_range = limit[len(prefix):-len(suffix)]
        else:
            start_range = start[len(prefix):]
            limit_range = limit[len(prefix):]

        if start_range >= limit_range:
            raise FeatureLibError(
                "Start of range must be smaller than its end",
                location)

        uppercase = re.compile(r'^[A-Z]$')
        if uppercase.match(start_range) and uppercase.match(limit_range):
            for c in range(ord(start_range), ord(limit_range) + 1):
                result.append("%s%c%s" % (prefix, c, suffix))
            return result

        lowercase = re.compile(r'^[a-z]$')
        if lowercase.match(start_range) and lowercase.match(limit_range):
            for c in range(ord(start_range), ord(limit_range) + 1):
                result.append("%s%c%s" % (prefix, c, suffix))
            return result

        digits = re.compile(r'^[0-9]{1,3}$')
        if digits.match(start_range) and digits.match(limit_range):
            for i in range(int(start_range, 10), int(limit_range, 10) + 1):
                number = ("000" + str(i))[-len(start_range):]
                result.append("%s%s%s" % (prefix, number, suffix))
            return result

        raise FeatureLibError("Bad range: \"%s-%s\"" % (start, limit),
                              location)


class SymbolTable(object):
    def __init__(self):
        self.scopes_ = [{}]

    def enter_scope(self):
        self.scopes_.append({})

    def exit_scope(self):
        self.scopes_.pop()

    def define(self, name, item):
        self.scopes_[-1][name] = item

    def resolve(self, name):
        for scope in reversed(self.scopes_):
            item = scope.get(name)
            if item:
                return item
        return None
