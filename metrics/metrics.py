import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, confusion_matrix, ConfusionMatrixDisplay, accuracy_score, \
    f1_score

from metrics.abstract_metric import AbstractMetric


class PrecisionMetric(AbstractMetric):
    def calculate(self):
        print("precision:", precision_score(self.y_true, self.y_pred))


class RecallMetric(AbstractMetric):
    def calculate(self):
        print("recall:", recall_score(self.y_true, self.y_pred))


class FalsePositiveMetric(AbstractMetric):
    def calculate(self):
        tn, fp, fn, tp = confusion_matrix(self.y_true, self.y_pred).ravel()
        print("false positive rate:", fp / (fp + tn))


class FalseNegativeMetric(AbstractMetric):
    def calculate(self):
        tn, fp, fn, tp = confusion_matrix(self.y_true, self.y_pred).ravel()
        print("false negative rate:", fn / (tp + fn))


class TrueNegativeMetric(AbstractMetric):
    def calculate(self):
        tn, fp, fn, tp = confusion_matrix(self.y_true, self.y_pred).ravel()
        print("true negative rate:", tn / (tn + fp))


class NegativePredictiveMetric(AbstractMetric):
    def calculate(self):
        tn, fp, fn, tp = confusion_matrix(self.y_true, self.y_pred).ravel()
        print("negative predictive value:", tn / (tn + fn))


class FalseDiscoveryMetric(AbstractMetric):
    def calculate(self):
        tn, fp, fn, tp = confusion_matrix(self.y_true, self.y_pred).ravel()
        print("false discovery rate:", fp / (tp + fp))


class TruePositiveMetric(AbstractMetric):
    def calculate(self):
        tn, fp, fn, tp = confusion_matrix(self.y_true, self.y_pred).ravel()
        print("true positive rate:", tp / (tp + fn))


class AccuracyMetric(AbstractMetric):
    def calculate(self):
        print("accuracy rate:", accuracy_score(self.y_true, self.y_pred))


class F1Metric(AbstractMetric):
    def calculate(self):
        print("f1 score:", f1_score(self.y_true, self.y_pred))


class ConfusionMetric(AbstractMetric):
    def calculate(self):
        cm = confusion_matrix(self.y_true, self.y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.show()
