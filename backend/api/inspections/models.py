from django.db import models

class Inspector(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)

class Inspection(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=25, null=True, blank=True)
    scheduledDate = models.DateTimeField(null=True, blank=True)
    inspectorId = models.ForeignKey(Inspector, on_delete=models.RESTRICT)
    Company = models.CharField(max_length=50, null=True, blank=True)
    @property
    def title (self):
        if self.scheduledDate:
            year = self.scheduledDate.year
            month = self.scheduledDate.month
            day = self.scheduledDate.day
        else:
            year = month = day = ""
        return f'{self.city} - {year}/{month}/{day}'
    @property
    def itemsOk (self):
        return self.item_set.filter(isIssue=False).count()
    @property
    def issuesWarningCount (self):
        return self.item_set.filter(severity__lt=60).count()
    @property
    def issuesCriticalCount (self):
        return self.item_set.filter(severity__gte=60).count()
    @property
    def inspectorName (self):
        return self.inspectorId.name

class Item(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    isIssue = models.BooleanField(null=True, blank=True)
    severity = models.PositiveSmallIntegerField(null=True, blank=True)
    label = models.CharField(max_length=50, null=True, blank=True)
    positionX = models.CharField(max_length=15, null=True, blank=True)
    positionY = models.CharField(max_length=15, null=True, blank=True)
    inspectionId = models.ForeignKey(Inspection, on_delete=models.RESTRICT)
