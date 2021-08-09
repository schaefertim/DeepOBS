from torch import nn

from ..datasets.svhn import svhn
from .testproblem import WeightRegularizedTestproblem
from .testproblems_modules import net_cifar10_3c3d


class svhn_3c3d(WeightRegularizedTestproblem):
    """DeepOBS test problem class for a three convolutional and three dense \
    layered neural network on SVHN.

  The network consists of

    - three conv layers with ReLUs, each followed by max-pooling
    - two fully-connected layers with ``512`` and ``256`` units and ReLU activation
    - 10-unit output layer with softmax
    - cross-entropy loss
    - L2 regularization on the weights (but not the biases) with a default
      factor of 0.002

  The weight matrices are initialized using Xavier initialization and the biases
  are initialized to ``0.0``.

  Args:
      batch_size (int): Batch size to use.
      l2_reg (float): L2-regularization factor. L2-Regularization (weight decay)
          is used on the weights but not the biases. Defaults to ``0.002``.

  Attributes:
    data: The DeepOBS data set class for SVHN.
    loss_function: The loss function for this testproblem is torch.nn.CrossEntropyLoss().
    net: The DeepOBS subclass of torch.nn.Module that is trained for this tesproblem (net_cifar10_3c3d with 10 outputs).
  """

    def __init__(self, batch_size, l2_reg=0.002):
        """Create a new 3c3d test problem instance on SVHN.

        Args:
            batch_size (int): Batch size to use.
            l2_reg (float): L2-regularization factor. L2-Regularization (weight decay)
                is used on the weights but not the biases. Defaults to ``0.002``.
        """

        super(svhn_3c3d, self).__init__(batch_size, l2_reg)

    def set_up(self):
        """Set up the vanilla CNN test problem on SVHN."""
        self.data = svhn(self._batch_size)
        self.loss_function = nn.CrossEntropyLoss
        self.net = net_cifar10_3c3d(num_outputs=10)
        self.net.to(self._device)
        self.regularization_groups = self.get_regularization_groups()