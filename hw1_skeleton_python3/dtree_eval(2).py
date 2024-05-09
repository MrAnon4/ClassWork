'''
    TEMPLATE FOR MACHINE LEARNING HOMEWORK
    AUTHOR Eric Eaton, Chris Clingerman
'''
import math
import numpy as np
import matplotlib.pyplot as plt

from sklearn import tree
from sklearn.metrics import accuracy_score

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit



def evaluatePerformance():
    '''
    Evaluate the performance of decision trees,
    averaged over 1,000 trials of 10-fold cross validation
    
    Return:
      a matrix giving the performance that will contain the following entries:
      stats[0,0] = mean accuracy of decision tree
      stats[0,1] = std deviation of decision tree accuracy
      stats[1,0] = mean accuracy of decision stump
      stats[1,1] = std deviation of decision stump
      stats[2,0] = mean accuracy of 3-level decision tree
      stats[2,1] = std deviation of 3-level decision tree
      
    ** Note that your implementation must follow this API**
    '''
    
    # Load Data
    filename = 'SPECTF.dat'
    data = np.loadtxt(filename, delimiter=',')
    X = data[:, 1:]
    y = np.array([data[:, 0]]).T
    n,d = X.shape

    scores = 0
    mean = 0
    meanin = 0
    axes = 0
    i = 0
    while i < 100:
      # shuffle the data
      idx = np.arange(n)
      np.random.seed(13)
      np.random.shuffle(idx)
      X = X[idx]
      y = y[idx]
      x = 0
    
      while x < 10:
        # split the data
        Xtrain = X[1:101,:]  # train on first 100 instances
        Xtest = X[101:,:]
        ytrain = y[1:101,:]  # test on remaining instances
        ytest = y[101:,:]

        # train the decision tree
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(Xtrain,ytrain)

        # output predictions on the remaining data
        y_pred = clf.predict(Xtest)

        clf2 = tree.DecisionTreeClassifier()
        clf2 = clf2.fit(Xtrain,ytrain)
        y_pred2 = clf2.predict(Xtest)

        clf3 = tree.DecisionTreeClassifier()
        clf3 = clf3.fit(Xtrain,ytrain)
        y_pred3 = clf3.predict(Xtest)

        clf4 = tree.DecisionTreeClassifier()
        clf4 = clf4.fit(Xtrain,ytrain)
        y_pred4 = clf4.predict(Xtest)

        clf5 = tree.DecisionTreeClassifier()
        clf5 = clf5.fit(Xtrain,ytrain)
        y_pred5 = clf5.predict(Xtest)

        clf6 = tree.DecisionTreeClassifier()
        clf6 = clf6.fit(Xtrain,ytrain)
        y_pred6 = clf6.predict(Xtest)

        
        # compute the training accuracy of the model
        meanDecisionTreeAccuracy = accuracy_score(ytest, y_pred)
        

      #  print(meanDecisionTreeAccuracy)

    
        tree.plot_tree(clf2, max_depth= 1)
        tree.plot_tree(clf3, max_depth= 2)
        tree.plot_tree(clf4, max_depth= 3)
        tree.plot_tree(clf5, max_depth= 4)
        tree.plot_tree(clf6, max_depth= 5)
        tree.plot_tree(clf)

        mean += meanDecisionTreeAccuracy
        meanin += meanDecisionTreeAccuracy - (mean/1000)
        meanin += meanin * meanin
        meanin = (meanin/1000)
        meanin = meanin/meanin +1 

        def plot_learning_curve(
        estimator,
        title,
        X,
        y,
        axes=None,
        ylim=None,
        cv=None,
        n_jobs=None,
        train_sizes=np.linspace(0.1, 1.0, 5),
        ):

              if axes is None:
                _, axes = plt.subplots(1, 3, figsize=(20, 5))

                axes[0].set_title(title)
                if ylim is not None:
                    axes[0].set_ylim(*ylim)
                axes[0].set_xlabel("Training examples")
                axes[0].set_ylabel("Score")

              train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(
                  estimator,
                  X,
                  y,
                  cv=cv,
                  n_jobs=n_jobs,
                  train_sizes=train_sizes,
                  return_times=True,
              )
              train_scores_mean = np.mean(train_scores, axis=1)
              train_scores_std = np.std(train_scores, axis=1)
              test_scores_mean = np.mean(test_scores, axis=1)
              test_scores_std = np.std(test_scores, axis=1)
              fit_times_mean = np.mean(fit_times, axis=1)
              fit_times_std = np.std(fit_times, axis=1)

              # Plot learning curve
              axes[0].grid()
              axes[0].fill_between(
                  train_sizes,
                  train_scores_mean - train_scores_std,
                  train_scores_mean + train_scores_std,
                  alpha=0.1,
                  color="r",
              )
              axes[0].fill_between(
                  train_sizes,
                  test_scores_mean - test_scores_std,
                  test_scores_mean + test_scores_std,
                  alpha=0.1,
                  color="g",
              )
              axes[0].plot(
                  train_sizes, train_scores_mean, "o-", color="r", label="Training score"
              )
              axes[0].plot(
                  train_sizes, test_scores_mean, "o-", color="g", label="Cross-validation score"
              )
              axes[0].legend(loc="best")

              plt.show()
      
      
        # TODO: update these statistics based on the results of your experiment
        stddevDecisionTreeAccuracy = 6 #math.sqrt(1/1000 *  (meanDecisionTreeAccuracy - mean_skill)^2 ) #np.std(accuracy_score(ytest, y_pred))
        meanDecisionStumpAccuracy = accuracy_score(ytest, y_pred)
        stddevDecisionStumpAccuracy = 6
        meanDT3Accuracy = accuracy_score(ytest, y_pred)
        stddevDT3Accuracy = 6 #math.sqrt(1/1000 * sum( (meanDecisionTreeAccuracy - mean_skill)^2 ))

        # make certain that the return value matches the API specification
        stats = np.zeros((3,2))
        stats[0,0] = meanDecisionTreeAccuracy
        stats[0,1] = stddevDecisionTreeAccuracy
        stats[1,0] = meanDecisionStumpAccuracy
        stats[1,1] = stddevDecisionStumpAccuracy
        stats[2,0] = meanDT3Accuracy
        stats[2,1] = stddevDT3Accuracy

        x += 1
      i+= 1


    
    return stats



# Do not modify from HERE...
if __name__ == "__main__":
    
    stats = evaluatePerformance()
    print("Decision Tree Accuracy = ", stats[0,0], " (", stats[0,1], ")")
    print("Decision Stump Accuracy = ", stats[1,0], " (", stats[1,1], ")")
    print("3-level Decision Tree = ", stats[2,0], " (", stats[2,1], ")")
# ...to HERE.



