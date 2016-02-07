import collections
import re
import ftfy

def LatexText():
    """Transform a unicode string into another more compatible with latex,
    fixing some common typographical errors"""
    text = LatexFixer(*args, **kwargs).tostring()
    return str(text)

class LatexFixer(collections.UserString):

    def __init__(self, text, frenchspacing=False):
      text = ftfy.fix_text(text)
      super().__init__(text)
      if not frenchspacing:
          self._sentence_to_interstitial_spacing()
          self._interstitial_to_sentence_spacing()
      self._latex_symbols()
      self._hyphens_to_dashes()

    def tostring(self):
      """Return self as instance of str()"""
      return self.data

    def _sentence_to_interstitial_spacing(self):
        """Fix common spacing errors caused by LaTeX's habit
        of using an inter-sentence space after any full stop."""

        not_sentence_end_chars = [' ']
        abbreviations = ['i.e.', 'e.g.', ' v.',
            ' w.', ' wh.']
        titles = ['Prof.', 'Mr.', 'Mrs.', 'Messrs.',
            'Mmes.', 'Msgr.', 'Ms.', 'Fr.', 'Rev.',
            'St.', 'Dr.', 'Lieut.', 'Lt.', 'Capt.',
            'Cptn.', 'Sgt.', 'Sjt.', 'Gen.', 'Hon.',
            'Cpl.', 'L-Cpl.', 'Pvt.', 'Dvr.', 'Gnr.',
            'Spr.', 'Col.', 'Lt-Col', 'Lt-Gen.', 'Mx.']

        for abbrev in abbreviations:
            for x in not_sentence_end_chars:
                self._str_replacement(abbrev + x, abbrev + '\ ')

        for title in titles:
            for x in not_sentence_end_chars:
                self._str_replacement(title + x, title + '~')

    def _interstitial_to_sentence_spacing(self):
      """Fix errors where inter-sentence spacing
      is not used after after a word ending with a capital letter.
      """
      pass

    def _latex_symbols(self):
      """Replace unicode symbols with latex commands
      where those symbols cannot be represented in utf mode."""

      substs = [('∴', '\\thinspace$\\therefore$\\thinspace{}'), # requires \amssymb
                ('...', '\dots{}'),
                ('÷', '$\div%')]
      for sub in substs:
          self._str_replacement(*sub)

    def _hyphens_to_dashes(self):
      """Transform hyphens to various kinds of dashes"""

      problematic_hyphens = [(r'-([.,!)])', r'---\1'),
                             (r'(?<=\d)-(?=\d)', '--'),
                             (r'(?<=\s)-(?=\s)', '---')]

      for problem_case in problematic_hyphens:
          self._regex_replacement(*problem_case)


    def _str_replacement(self, target, replacement):
      """Replace target with replacement"""
      self.data = self.data.replace(target, replacement)

    def _regex_replacement(self, target, replacement):
      """Regex substitute target with replacement"""
      match = re.compile(target)
      self.data = match.sub(replacement, self.data)
